#!/usr/bin/env python3

import os
import logging
import defectdojo_api


def main():
    log_level = os.getenv("DEVSECOPS_TOOLS_LOG_LEVEL", "INFO")
    logging.basicConfig(level=log_level)

    active_findings_logger = logging.getLogger("defectdojo_active_findings")
    env_defect_dojo_url = os.getenv("DEFECT_DOJO_URL", None)
    env_defect_dojo_username = os.getenv("DEFECT_DOJO_USERNAME", None)
    env_defect_dojo_password = os.getenv("DEFECT_DOJO_PASSWORD", None)
    env_defect_dojo_product = os.getenv("DEFECT_DOJO_PRODUCT", None)
    env_client_certificate_file_path = os.getenv("CLIENT_CERTIFICATE_FILE_PATH", None)
    env_client_key_file_path = os.getenv("CLIENT_KEY_FILE_PATH", None)

    active_findings_logger.info(
        f"requesting authentication token from {env_defect_dojo_url}"
    )

    defect_dojo_api_token = defectdojo_api.retrieve_defectdojo_token(
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_username=env_defect_dojo_username,
        defect_dojo_password=env_defect_dojo_password,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=active_findings_logger,
    )

    active_findings_logger.info("authentication token retrieved successfully")

    active_findings_logger.info(f"querying findings for {env_defect_dojo_product}")

    findings = defectdojo_api.number_of_open_findings_defectdojo(
        defect_dojo_product=env_defect_dojo_product,
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_token=defect_dojo_api_token,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=active_findings_logger,
    )

    active_findings_logger.info(f"{env_defect_dojo_product} has {findings} open")

    os.system(f"echo 'open_findings={findings}' >> $GITHUB_OUTPUT")


if __name__ == "__main__":
    main()

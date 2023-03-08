#!/usr/bin/env python3

import os
import logging
import defectdojo.src.defectdojo_api as defectdojo_api


def main():
    log_level = os.getenv("DEVSECOPS_TOOLS_LOG_LEVEL", "INFO")
    logging.basicConfig(level=log_level)

    upload_scan_logger = logging.getLogger("defectdojo_upload_scan")
    env_defect_dojo_url = os.getenv("DEFECT_DOJO_URL", None)
    env_defect_dojo_username = os.getenv("DEFECT_DOJO_USERNAME", None)
    env_defect_dojo_password = os.getenv("DEFECT_DOJO_PASSWORD", None)
    env_defect_dojo_product_type = os.getenv("DEFECT_DOJO_PRODUCT_TYPE", None)
    env_defect_dojo_product = os.getenv("DEFECT_DOJO_PRODUCT", None)
    env_defect_dojo_environment_type = os.getenv("DEFECT_DOJO_ENVIRONMENT_TYPE", None)
    env_defect_dojo_scan_type = os.getenv("DEFECT_DOJO_SCAN_TYPE", None)
    env_defect_dojo_engagement_name = os.getenv("DEFECT_DOJO_ENGAGEMENT_NAME", None)

    env_scan_results_file_path = os.getenv("SCAN_RESULTS_FILE_PATH", None)
    env_client_certificate_file_path = os.getenv("CLIENT_CERTIFICATE_FILE_PATH", None)
    env_client_key_file_path = os.getenv("CLIENT_KEY_FILE_PATH", None)

    upload_scan_logger.info(
        f"requesting authentication token from {env_defect_dojo_url}"
    )

    defect_dojo_api_token = defectdojo_api.retrieve_defectdojo_token(
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_username=env_defect_dojo_username,
        defect_dojo_password=env_defect_dojo_password,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=upload_scan_logger,
    )

    upload_scan_logger.info("authentication token retrieved successfully")

    upload_scan_logger.info(f"importing {env_defect_dojo_scan_type}")

    defectdojo_api.import_scan_results_to_defectdojo(
        defect_dojo_product_type=env_defect_dojo_product_type,
        defect_dojo_product=env_defect_dojo_product,
        defect_dojo_environment_type=env_defect_dojo_environment_type,
        defect_dojo_scan_type=env_defect_dojo_scan_type,
        defect_dojo_engagement_name=env_defect_dojo_engagement_name,
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_token=defect_dojo_api_token,
        scan_results_file_path=env_scan_results_file_path,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=upload_scan_logger,
    )

    upload_scan_logger.info(f"{env_defect_dojo_scan_type} successfully imported")


if __name__ == "__main__":
    main()

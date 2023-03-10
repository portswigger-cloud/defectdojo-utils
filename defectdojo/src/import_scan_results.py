#!/usr/bin/env python3

import logging
import defectdojo_api
import collect_common_data


def main():
    env_vars = collect_common_data.get_common_env_vars()

    log_level = env_vars["log_level"]
    env_defect_dojo_url = env_vars["env_defect_dojo_url"]
    env_defect_dojo_username = env_vars["env_defect_dojo_username"]
    env_defect_dojo_password = env_vars["env_defect_dojo_password"]
    env_defect_dojo_product_type = env_vars["env_defect_dojo_product_type"]
    env_defect_dojo_product = env_vars["env_defect_dojo_product"]
    env_defect_dojo_environment_type = env_vars["env_defect_dojo_environment_type"]
    env_defect_dojo_scan_type = env_vars["env_defect_dojo_scan_type"]
    env_defect_dojo_engagement_name = env_vars["env_defect_dojo_engagement_name"]
    env_scan_results_file_path = env_vars["env_scan_results_file_path"]
    env_client_certificate_file_path = env_vars["env_client_certificate_file_path"]
    env_client_key_file_path = env_vars["env_client_key_file_path"]

    logging.basicConfig(level=log_level)
    upload_scan_logger = logging.getLogger("defectdojo_upload_scan")

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

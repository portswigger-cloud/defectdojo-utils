#!/usr/bin/env python3

import os
import sys
import logging
from collections import Counter
import defectdojo_api
import github_actions
import findings_thresholds


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
    env_create_github_outputs = os.getenv("CREATE_GITHUB_OUTPUTS", True)
    env_create_github_step_summary = os.getenv("CREATE_GITHUB_STEP_SUMMARY", True)
    env_enable_thresholds = os.getenv("ENABLE_THRESHOLDS", False)

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

    findings_count = defectdojo_api.get_findings_count_defectdojo(
        defect_dojo_product=env_defect_dojo_product,
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_token=defect_dojo_api_token,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=active_findings_logger,
    )

    findings = defectdojo_api.get_findings_defectdojo(
        defect_dojo_product=env_defect_dojo_product,
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_token=defect_dojo_api_token,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=active_findings_logger,
        limit=findings_count,
    )

    results = findings["results"]
    severity_raw = []
    for items in results:
        severity_raw.append(items["severity"])
    severity_sum = Counter(severity_raw)

    findings_summary = {
        "total": sum(severity_sum.values()),
        "critical": severity_sum["Critical"],
        "high": severity_sum["High"],
        "medium": severity_sum["Medium"],
        "low": severity_sum["Low"],
        "info": severity_sum["Info"],
    }

    step_summary_data = findings_summary.copy()
    step_summary_data["product"] = env_defect_dojo_product
    if env_create_github_outputs:
        github_actions.set_action_outputs(findings_summary)
    if env_create_github_step_summary:
        github_actions.active_findings_markdown_step_summary(**step_summary_data)
    if env_enable_thresholds:
        env_thresholds = {
            "total": os.getenv("TOTAL_THRESHOLD", None),
            "critical": os.getenv("CRITICAL_THRESHOLD", None),
            "high": os.getenv("HIGH_THRESHOLD", None),
            "medium": os.getenv("MEDIUM_THRESHOLD", None),
            "low": os.getenv("LOW_THRESHOLD", None),
            "info": os.getenv("INFO_THRESHOLD", None),
        }
        failed_threshold = findings_thresholds.evaluate_thresholds(
            findings_summary, env_thresholds
        )
        if failed_threshold is True:
            sys.exit(2)


if __name__ == "__main__":
    main()

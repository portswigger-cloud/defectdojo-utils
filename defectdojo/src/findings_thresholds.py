#!/usr/bin/env python3

import sys
import logging
from collections import Counter
import collect_common_data
import defectdojo_api
import github_actions
import findings_thresholds


def evaluate_thresholds(active_findings: dict, findings_thresholds: dict) -> bool:
    counter: int = 0
    if findings_thresholds["total"] != "false":
        if active_findings["total"] > int(findings_thresholds["total"]):
            github_actions.total_findings_threshold_markdown_step_summary(
                active_findings["total"], findings_thresholds["total"]
            )
            counter = counter + 1
    if findings_thresholds["total"] != "false":
        if active_findings["critical"] > int(findings_thresholds["critical"]):
            github_actions.severity_findings_threshold_markdown_step_summary(
                "critical", active_findings["critical"], findings_thresholds["critical"]
            )
            counter = counter + 1

    if findings_thresholds["total"] != "false":
        if active_findings["high"] > int(findings_thresholds["high"]):
            github_actions.severity_findings_threshold_markdown_step_summary(
                "high", active_findings["high"], findings_thresholds["high"]
            )
            counter = counter + 1
    if findings_thresholds["total"] != "false":
        if active_findings["medium"] > int(findings_thresholds["medium"]):
            github_actions.severity_findings_threshold_markdown_step_summary(
                "medium", active_findings["medium"], findings_thresholds["medium"]
            )
            counter = counter + 1
    if findings_thresholds["total"] != "false":
        if active_findings["low"] > int(findings_thresholds["low"]):
            github_actions.severity_findings_threshold_markdown_step_summary(
                "low", active_findings["low"], findings_thresholds["low"]
            )
            counter = counter + 1
    if findings_thresholds["total"] != "false":
        if active_findings["info"] > int(findings_thresholds["info"]):
            github_actions.severity_findings_threshold_markdown_step_summary(
                "info", active_findings["info"], findings_thresholds["info"]
            )
            counter = counter + 1
    if counter > 0:
        return True
    else:
        return False


def main():
    env_vars = collect_common_data.get_common_env_vars()
    log_level = env_vars["log_level"]
    env_defect_dojo_url = env_vars["env_defect_dojo_url"]
    env_defect_dojo_username = env_vars["env_defect_dojo_username"]
    env_defect_dojo_password = env_vars["env_defect_dojo_password"]
    env_defect_dojo_product = env_vars["env_defect_dojo_product"]
    env_client_certificate_file_path = env_vars["env_client_certificate_file_path"]
    env_client_key_file_path = env_vars["env_client_key_file_path"]

    logging.basicConfig(level=log_level)
    findings_thresholds_logger = logging.getLogger("defectdojo_findings_thresholds")

    findings_thresholds_logger.info(
        f"requesting authentication token from {env_defect_dojo_url}"
    )

    defect_dojo_api_token = defectdojo_api.retrieve_defectdojo_token(
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_username=env_defect_dojo_username,
        defect_dojo_password=env_defect_dojo_password,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=findings_thresholds_logger,
    )

    findings_thresholds_logger.info("authentication token retrieved successfully")

    findings_thresholds_logger.info(f"querying findings for {env_defect_dojo_product}")

    findings_count = defectdojo_api.get_findings_count_defectdojo(
        defect_dojo_product=env_defect_dojo_product,
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_token=defect_dojo_api_token,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=findings_thresholds_logger,
    )

    findings = defectdojo_api.get_findings_defectdojo(
        defect_dojo_product=env_defect_dojo_product,
        defect_dojo_url=env_defect_dojo_url,
        defect_dojo_token=defect_dojo_api_token,
        client_certificate_file_path=env_client_certificate_file_path,
        client_key_file_path=env_client_key_file_path,
        logger=findings_thresholds_logger,
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

    env_thresholds = {
        "total": env_vars["total"],
        "critical": env_vars["critical"],
        "high": env_vars["high"],
        "medium": env_vars["medium"],
        "low": env_vars["low"],
        "info": env_vars["info"],
    }
    findings_thresholds_logger.info("checking thresholds")
    failed_threshold = findings_thresholds.evaluate_thresholds(
        findings_summary, env_thresholds
    )
    if failed_threshold is True:
        sys.exit(2)
    elif failed_threshold is False:
        findings_thresholds_logger.info(
            f"The thresholds for active findings for {env_defect_dojo_product} haven't been exceeded"
        )


if __name__ == "__main__":
    main()

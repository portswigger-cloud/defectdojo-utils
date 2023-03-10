import os


def get_common_env_vars() -> dict:
    return {
        "log_level": os.getenv("DEVSECOPS_TOOLS_LOG_LEVEL", "INFO"),
        "env_defect_dojo_url": os.getenv("DEFECT_DOJO_URL", None),
        "env_defect_dojo_username": os.getenv("DEFECT_DOJO_USERNAME", None),
        "env_defect_dojo_password": os.getenv("DEFECT_DOJO_PASSWORD", None),
        "env_defect_dojo_product_type": os.getenv("DEFECT_DOJO_PRODUCT_TYPE", None),
        "env_defect_dojo_product": os.getenv("DEFECT_DOJO_PRODUCT", None),
        "env_defect_dojo_environment_type": os.getenv(
            "DEFECT_DOJO_ENVIRONMENT_TYPE", None
        ),
        "env_defect_dojo_scan_type": os.getenv("DEFECT_DOJO_SCAN_TYPE", None),
        "env_defect_dojo_engagement_name": os.getenv(
            "DEFECT_DOJO_ENGAGEMENT_NAME", None
        ),
        "env_scan_results_file_path": os.getenv("SCAN_RESULTS_FILE_PATH", None),
        "env_client_certificate_file_path": os.getenv(
            "CLIENT_CERTIFICATE_FILE_PATH", None
        ),
        "env_client_key_file_path": os.getenv("CLIENT_KEY_FILE_PATH", None),
        "total": os.getenv("TOTAL_THRESHOLD", "false"),
        "critical": os.getenv("CRITICAL_THRESHOLD", "false"),
        "high": os.getenv("HIGH_THRESHOLD", "false"),
        "medium": os.getenv("MEDIUM_THRESHOLD", "false"),
        "low": os.getenv("LOW_THRESHOLD", "false"),
        "info": os.getenv("INFO_THRESHOLD", "false"),
        "env_create_github_outputs": os.getenv("CREATE_GITHUB_OUTPUTS", "False"),
    }

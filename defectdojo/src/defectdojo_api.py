import requests
import json
import sys
import logging

requests_timeout = 120


def retrieve_defectdojo_token(
    defect_dojo_url: str,
    defect_dojo_username: str,
    defect_dojo_password: str,
    client_certificate_file_path: str,
    client_key_file_path: str,
    logger: logging.Logger,
) -> str:
    data = {"username": defect_dojo_username, "password": defect_dojo_password}

    api_endpoint = f"{defect_dojo_url}api/v2/api-token-auth/"

    if client_certificate_file_path and client_key_file_path:
        r = requests.post(
            api_endpoint,
            data=data,
            verify=True,
            cert=(client_certificate_file_path, client_key_file_path),
            timeout=requests_timeout,
        )
    elif not client_certificate_file_path and not client_key_file_path:
        r = requests.post(
            api_endpoint,
            data=data,
            verify=True,
            timeout=requests_timeout,
        )
    else:
        logger.error(
            "either the client certificate or client key file paths were not set correctly"
        )
        sys.exit(1)

    if r.status_code == 200:
        return (json.loads(r.text))["token"]
    else:
        logger.error(f"authentication to {defect_dojo_url} failed")
        sys.exit(1)


def import_scan_results_to_defectdojo(
    defect_dojo_product_type: str,
    defect_dojo_product: str,
    defect_dojo_environment_type: str,
    defect_dojo_scan_type: str,
    defect_dojo_engagement_name: str,
    defect_dojo_url: str,
    defect_dojo_token: str,
    scan_results_file_path: str,
    client_certificate_file_path: str,
    client_key_file_path: str,
    logger: logging.Logger,
) -> int:
    headers = {
        "Authorization": f"Token {defect_dojo_token}",
    }

    api_endpoint = f"{defect_dojo_url}api/v2/import-scan/"

    files = {}
    files["file"] = open(scan_results_file_path)

    data = {
        "product_type_name": defect_dojo_product_type,
        "product_name": defect_dojo_product,
        "environment": defect_dojo_environment_type,
        "scan_type": defect_dojo_scan_type,
        "engagement_name": defect_dojo_engagement_name,
        "auto_create_context": True,
        "close_old_findings": True,
        "verified": False,
    }
    if client_certificate_file_path and client_key_file_path:
        r = requests.post(
            api_endpoint,
            headers=headers,
            files=files,
            data=data,
            verify=True,
            cert=(client_certificate_file_path, client_key_file_path),
            timeout=requests_timeout,
        )
    elif not client_certificate_file_path and not client_key_file_path:
        r = requests.post(
            api_endpoint,
            headers=headers,
            files=files,
            data=data,
            verify=True,
            timeout=requests_timeout,
        )
    else:
        logger.error(
            "either the client certificate or client key file paths were not set correctly"
        )
        sys.exit(1)
    if r.status_code == 201:
        return r.status_code
    else:
        logger.error(f"upload of results to {defect_dojo_url} failed")
        sys.exit(1)


def get_findings_count_defectdojo(
    defect_dojo_product: str,
    defect_dojo_url: str,
    defect_dojo_token: str,
    client_certificate_file_path: str,
    client_key_file_path: str,
    logger: logging.Logger,
) -> int:
    headers: dict = {
        "Authorization": f"Token {defect_dojo_token}",
    }

    api_endpoint = f"{defect_dojo_url}api/v2/findings/?active=true&product_name={defect_dojo_product}"

    if client_certificate_file_path and client_key_file_path:
        r = requests.get(
            api_endpoint,
            headers=headers,
            verify=True,
            cert=(client_certificate_file_path, client_key_file_path),
            timeout=requests_timeout,
        )

    elif not client_certificate_file_path and not client_key_file_path:
        r = requests.get(
            api_endpoint,
            headers=headers,
            verify=True,
            timeout=requests_timeout,
        )

    else:
        logger.error(
            "either the client certificate or client key file paths were not set correctly"
        )
        sys.exit(1)
    if r.status_code == 200:
        return json.loads(r.text)["count"]

    else:
        logger.error(f"get open findings for product {defect_dojo_product} failed")
        sys.exit(1)


def get_findings_defectdojo(
    defect_dojo_product: str,
    defect_dojo_url: str,
    defect_dojo_token: str,
    client_certificate_file_path: str,
    client_key_file_path: str,
    limit: int,
    logger: logging.Logger,
) -> dict:
    headers: dict = {
        "Authorization": f"Token {defect_dojo_token}",
    }

    api_endpoint = f"{defect_dojo_url}api/v2/findings/?active=true&limit={limit}&product_name={defect_dojo_product}"

    if client_certificate_file_path and client_key_file_path:
        r = requests.get(
            api_endpoint,
            headers=headers,
            verify=True,
            cert=(client_certificate_file_path, client_key_file_path),
            timeout=requests_timeout,
        )

    elif not client_certificate_file_path and not client_key_file_path:
        r = requests.get(
            api_endpoint,
            headers=headers,
            verify=True,
            timeout=requests_timeout,
        )

    else:
        logger.error(
            "either the client certificate or client key file paths were not set correctly"
        )
        sys.exit(1)
    if r.status_code == 200:
        return json.loads(r.text)

    else:
        logger.error(f"get open findings for product {defect_dojo_product} failed")
        sys.exit(1)

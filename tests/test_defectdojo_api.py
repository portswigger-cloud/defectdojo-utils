import json
import pytest
import logging
import defectdojo.src.defectdojo_api as defectdojo_api


@pytest.fixture
def logging_setup():
    logging.basicConfig(level="DEBUG")
    logger = logging.getLogger("PYTEST")
    return logger


@pytest.fixture
def setup_retrieve_defectdojo_token_data():
    yield {
        "defect_dojo_url": "https://defectdojo.example.com/",
        "defect_dojo_username": "testuser",
        "defect_dojo_password": "password",
    }


@pytest.fixture
def setup_number_of_open_finding():
    yield {
        "defect_dojo_product": "wobble product",
        "defect_dojo_token": "4e3d91c12f87a5de17488881fce619862f360d99",
        "defect_dojo_url": "https://defectdojo.example.com/",
        "limit": 100,
    }


@pytest.fixture
def setup_cert_data_no_cert():
    yield {
        "client_certificate_file_path": None,
        "client_key_file_path": None,
    }


@pytest.fixture
def setup_cert_data_cert():
    yield {
        "client_certificate_file_path": "defectdojo_send_scan/tests/data/dummy.cert",
        "client_key_file_path": "defectdojo_send_scan/tests/data/dummy.key",
    }


@pytest.fixture
def setup_cert_data_cert_missing_key():
    yield {
        "client_certificate_file_path": "defectdojo_send_scan/tests/data/dummy.cert",
        "client_key_file_path": None,
    }


@pytest.fixture
def setup_cert_data_cert_missing_cert():
    yield {
        "client_certificate_file_path": None,
        "client_key_file_path": "defectdojo_send_scan/tests/data/dummy.key",
    }


@pytest.fixture
def setup_send_scan_results_to_defectdojo_data():
    yield {
        "defect_dojo_product_type": "wibble team",
        "defect_dojo_product": "wobble product",
        "defect_dojo_environment_type": "wibble environment",
        "defect_dojo_scan_type": "wobble scan",
        "defect_dojo_engagement_name": "wibble engagement",
        "defect_dojo_url": "https://defectdojo.example.com/",
        "defect_dojo_token": "4e3d91c12f87a5de17488881fce619862f360d99",
        "scan_results_file_path": "tests/data/dummy_scan_data.js",
    }


@pytest.fixture
def defectdojo_url():
    yield "https://defectdojo.example.com/"


@pytest.fixture
def retrieve_defectdojo_token_api_endpoint(defectdojo_url):
    yield f"{defectdojo_url}api/v2/api-token-auth/"


@pytest.fixture
def send_scan_results_to_defectdojo_api_endpoint(defectdojo_url):
    yield f"{defectdojo_url}api/v2/import-scan/"


@pytest.fixture
def findings_defectdojo_api_endpoint(defectdojo_url):
    yield f"{defectdojo_url}api/v2/findings/"


@pytest.fixture
def finding_response_data_no_findings():
    yield {
        "count": 0,
        "next": "null",
        "previous": "null",
        "results": [],
        "prefetch": {},
    }


@pytest.fixture
def finding_response_data_findings():
    with open("tests/data/findings.json") as json_file:
        findings_data = json.load(json_file)
        yield findings_data


def test_retrieve_defectdojo_token_no_cert_success(
    requests_mock,
    setup_cert_data_no_cert,
    setup_retrieve_defectdojo_token_data,
    retrieve_defectdojo_token_api_endpoint,
    logging_setup,
):
    expected = "4e3d91c12f87a5de17488881fce619862f360d99"
    mock_data = {"token": "4e3d91c12f87a5de17488881fce619862f360d99"}
    mock_status_code = 200
    requests_mock.post(
        retrieve_defectdojo_token_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )
    result = defectdojo_api.retrieve_defectdojo_token(
        logger=logging_setup,
        **setup_cert_data_no_cert,
        **setup_retrieve_defectdojo_token_data,
    )
    assert result == expected


def test_retrieve_defectdojo_token_cert_success(
    requests_mock,
    setup_cert_data_cert,
    setup_retrieve_defectdojo_token_data,
    retrieve_defectdojo_token_api_endpoint,
    logging_setup,
):
    expected = "4e3d91c12f87a5de17488881fce619862f360d99"
    mock_data = {"token": "4e3d91c12f87a5de17488881fce619862f360d99"}
    mock_status_code = 200
    requests_mock.post(
        retrieve_defectdojo_token_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )
    result = defectdojo_api.retrieve_defectdojo_token(
        logger=logging_setup,
        **setup_cert_data_cert,
        **setup_retrieve_defectdojo_token_data,
    )
    assert result == expected


def test_retrieve_defectdojo_token_cert_missing_key(
    requests_mock,
    setup_cert_data_cert_missing_key,
    setup_retrieve_defectdojo_token_data,
    retrieve_defectdojo_token_api_endpoint,
    logging_setup,
):
    mock_data = {"token": "4e3d91c12f87a5de17488881fce619862f360d99"}
    mock_status_code = 200
    requests_mock.post(
        retrieve_defectdojo_token_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.retrieve_defectdojo_token(
            logger=logging_setup,
            **setup_cert_data_cert_missing_key,
            **setup_retrieve_defectdojo_token_data,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_retrieve_defectdojo_token_cert_missing_cert(
    requests_mock,
    setup_cert_data_cert_missing_cert,
    setup_retrieve_defectdojo_token_data,
    retrieve_defectdojo_token_api_endpoint,
    logging_setup,
):
    mock_data = {"token": "4e3d91c12f87a5de17488881fce619862f360d99"}
    mock_status_code = 200
    requests_mock.post(
        retrieve_defectdojo_token_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.retrieve_defectdojo_token(
            logger=logging_setup,
            **setup_cert_data_cert_missing_cert,
            **setup_retrieve_defectdojo_token_data,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_retrieve_defectdojo_token_server_side_error(
    requests_mock,
    setup_cert_data_no_cert,
    setup_retrieve_defectdojo_token_data,
    retrieve_defectdojo_token_api_endpoint,
    logging_setup,
):
    mock_status_code = 500
    requests_mock.post(
        retrieve_defectdojo_token_api_endpoint,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.retrieve_defectdojo_token(
            logger=logging_setup,
            **setup_cert_data_no_cert,
            **setup_retrieve_defectdojo_token_data,
        )
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_send_scan_results_to_defectdojo_no_cert_success(
    requests_mock,
    setup_cert_data_no_cert,
    setup_send_scan_results_to_defectdojo_data,
    logging_setup,
    send_scan_results_to_defectdojo_api_endpoint,
):
    mock_status_code = 201
    expected = 201
    requests_mock.post(
        send_scan_results_to_defectdojo_api_endpoint,
        status_code=mock_status_code,
    )
    result = defectdojo_api.import_scan_results_to_defectdojo(
        logger=logging_setup,
        **setup_cert_data_no_cert,
        **setup_send_scan_results_to_defectdojo_data,
    )
    assert result == expected


def test_send_scan_results_to_defectdojo_server_side_error(
    requests_mock,
    setup_cert_data_no_cert,
    setup_send_scan_results_to_defectdojo_data,
    logging_setup,
    send_scan_results_to_defectdojo_api_endpoint,
):
    mock_status_code = 500
    requests_mock.post(
        send_scan_results_to_defectdojo_api_endpoint,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.import_scan_results_to_defectdojo(
            logger=logging_setup,
            **setup_cert_data_no_cert,
            **setup_send_scan_results_to_defectdojo_data,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_send_scan_results_to_defectdojo_cert_success(
    requests_mock,
    setup_cert_data_cert,
    setup_send_scan_results_to_defectdojo_data,
    logging_setup,
    send_scan_results_to_defectdojo_api_endpoint,
):
    mock_status_code = 201
    expected = 201
    requests_mock.post(
        send_scan_results_to_defectdojo_api_endpoint,
        status_code=mock_status_code,
    )
    result = defectdojo_api.import_scan_results_to_defectdojo(
        logger=logging_setup,
        **setup_cert_data_cert,
        **setup_send_scan_results_to_defectdojo_data,
    )
    assert result == expected


def test_send_scan_results_to_defectdojo_cert_fail_missing_key(
    requests_mock,
    setup_cert_data_cert_missing_key,
    setup_send_scan_results_to_defectdojo_data,
    logging_setup,
    send_scan_results_to_defectdojo_api_endpoint,
):
    mock_status_code = 201
    requests_mock.post(
        send_scan_results_to_defectdojo_api_endpoint,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.import_scan_results_to_defectdojo(
            logger=logging_setup,
            **setup_cert_data_cert_missing_key,
            **setup_send_scan_results_to_defectdojo_data,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_send_scan_results_to_defectdojo_cert_fail_missing_cert(
    requests_mock,
    setup_cert_data_cert_missing_cert,
    setup_send_scan_results_to_defectdojo_data,
    logging_setup,
    send_scan_results_to_defectdojo_api_endpoint,
):
    mock_status_code = 201
    requests_mock.post(
        send_scan_results_to_defectdojo_api_endpoint,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.import_scan_results_to_defectdojo(
            logger=logging_setup,
            **setup_cert_data_cert_missing_cert,
            **setup_send_scan_results_to_defectdojo_data,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_number_of_open_findings_no_cert_success(
    requests_mock,
    setup_cert_data_no_cert,
    setup_number_of_open_finding,
    findings_defectdojo_api_endpoint,
    finding_response_data_no_findings,
    logging_setup,
):
    mock_data = finding_response_data_no_findings
    mock_status_code = 200
    requests_mock.get(
        findings_defectdojo_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )
    result = defectdojo_api.get_findings_defectdojo(
        logger=logging_setup, **setup_cert_data_no_cert, **setup_number_of_open_finding
    )
    assert result == finding_response_data_no_findings


def test_number_of_open_findings_cert_success(
    requests_mock,
    setup_cert_data_cert,
    setup_number_of_open_finding,
    findings_defectdojo_api_endpoint,
    finding_response_data_no_findings,
    logging_setup,
):
    mock_data = finding_response_data_no_findings
    mock_status_code = 200
    requests_mock.get(
        findings_defectdojo_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )
    result = defectdojo_api.get_findings_defectdojo(
        logger=logging_setup, **setup_cert_data_cert, **setup_number_of_open_finding
    )
    assert result == finding_response_data_no_findings


def test_number_of_open_findings_cert_fail_missing_cert(
    requests_mock,
    setup_cert_data_cert_missing_cert,
    setup_number_of_open_finding,
    findings_defectdojo_api_endpoint,
    finding_response_data_no_findings,
    logging_setup,
):
    mock_data = finding_response_data_no_findings
    mock_status_code = 200
    requests_mock.get(
        findings_defectdojo_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.get_findings_defectdojo(
            logger=logging_setup,
            **setup_cert_data_cert_missing_cert,
            **setup_number_of_open_finding,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_number_of_open_findings_cert_fail_missing_key(
    requests_mock,
    setup_cert_data_cert_missing_key,
    setup_number_of_open_finding,
    findings_defectdojo_api_endpoint,
    finding_response_data_no_findings,
    logging_setup,
):
    mock_data = finding_response_data_no_findings
    mock_status_code = 200
    requests_mock.get(
        findings_defectdojo_api_endpoint,
        json=mock_data,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.get_findings_defectdojo(
            logger=logging_setup,
            **setup_cert_data_cert_missing_key,
            **setup_number_of_open_finding,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_number_of_open_findings_no_cert_fail_server_side_error(
    requests_mock,
    setup_cert_data_no_cert,
    setup_number_of_open_finding,
    findings_defectdojo_api_endpoint,
    logging_setup,
):
    mock_status_code = 500
    requests_mock.get(
        findings_defectdojo_api_endpoint,
        status_code=mock_status_code,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        defectdojo_api.get_findings_defectdojo(
            logger=logging_setup,
            **setup_cert_data_no_cert,
            **setup_number_of_open_finding,
        )

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

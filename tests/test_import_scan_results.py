import os
import pytest
import defectdojo.src.import_scan_results as import_scan_results


@pytest.fixture
def defect_dojo_url_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_URL"] = "www.defectdojo.example.com"
    yield os.environ["DEFECT_DOJO_URL"]


@pytest.fixture
def defect_dojo_username_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_USERNAME"] = "test-user"
    yield os.environ["DEFECT_DOJO_USERNAME"]


@pytest.fixture
def defect_dojo_password_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_PASSWORD"] = "test-password"
    yield os.environ["DEFECT_DOJO_PASSWORD"]


@pytest.fixture
def defect_dojo_product_type_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_PRODUCT_TYPE"] = "test-product-type"
    yield os.environ["DEFECT_DOJO_PRODUCT_TYPE"]


@pytest.fixture
def defect_dojo_product_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_PRODUCT"] = "test-product"
    yield os.environ["DEFECT_DOJO_PRODUCT"]


@pytest.fixture
def defect_dojo_environment_type_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_ENVIRONMENT_TYPE"] = "test-environment-type"
    yield os.environ["DEFECT_DOJO_ENVIRONMENT_TYPE"]


@pytest.fixture
def defect_dojo_scan_type_env_var() -> pytest.fixture():
    os.environ["DEFECT_DOJO_SCAN_TYPE"] = "test-scan-type"
    yield os.environ["DEFECT_DOJO_SCAN_TYPE"]


@pytest.fixture
def scan_results_file_path_env_var(tmpdir) -> pytest.fixture():
    os.environ["SCAN_RESULTS_FILE_PATH"] = f"{tmpdir}/scan-results.json"
    yield os.environ["SCAN_RESULTS_FILE_PATH"]


@pytest.fixture
def client_certificate_file_path_env_var(tmpdir) -> pytest.fixture():
    os.environ["CLIENT_CERTIFICATE_FILE_PATH"] = f"{tmpdir}/test.cert"
    yield os.environ["CLIENT_CERTIFICATE_FILE_PATH"]


@pytest.fixture
def client_key_file_path_env_var(tmpdir) -> pytest.fixture():
    os.environ["CLIENT_KEY_FILE_PATH"] = f"{tmpdir}/test.key"
    yield os.environ["CLIENT_KEY_FILE_PATH"]


def test_main_no_cert(
    mocker,
    defect_dojo_url_env_var,
    defect_dojo_username_env_var,
    defect_dojo_password_env_var,
    defect_dojo_product_type_env_var,
    defect_dojo_product_env_var,
    defect_dojo_environment_type_env_var,
    defect_dojo_scan_type_env_var,
    scan_results_file_path_env_var,
):
    mocker.patch(
        "defectdojo.src.import_scan_results.defectdojo_api.retrieve_defectdojo_token",
        return_value="d11dc2d650168f488e6143b6fa428483fbc7de29",
    )
    mocker.patch(
        "defectdojo.src.import_scan_results.defectdojo_api.import_scan_results_to_defectdojo",
        return_value=201,
    )
    result = import_scan_results.main()
    assert result is None


def test_main_cert(
    mocker,
    defect_dojo_url_env_var,
    defect_dojo_username_env_var,
    defect_dojo_password_env_var,
    defect_dojo_product_type_env_var,
    defect_dojo_product_env_var,
    defect_dojo_environment_type_env_var,
    defect_dojo_scan_type_env_var,
    scan_results_file_path_env_var,
    client_certificate_file_path_env_var,
    client_key_file_path_env_var,
):
    mocker.patch(
        "defectdojo.src.import_scan_results.defectdojo_api.retrieve_defectdojo_token",
        return_value="d11dc2d650168f488e6143b6fa428483fbc7de29",
    )
    mocker.patch(
        "defectdojo.src.import_scan_results.defectdojo_api.import_scan_results_to_defectdojo",
        return_value=201,
    )
    result = import_scan_results.main()
    assert result is None

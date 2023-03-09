import defectdojo.src.import_scan_results as import_scan_results


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

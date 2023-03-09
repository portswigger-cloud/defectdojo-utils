import os
import pytest
import defectdojo.src.active_findings as active_findings


@pytest.fixture
def env_create_github_outputs_false_env_var():
    os.environ["CREATE_GITHUB_OUTPUTS"] = "False"
    yield os.environ["CREATE_GITHUB_OUTPUTS"]


@pytest.fixture
def env_create_github_step_summary_false_env_var():
    os.environ["CREATE_GITHUB_STEP_SUMMARY"] = "False"
    yield os.environ["CREATE_GITHUB_STEP_SUMMARY"]


@pytest.fixture
def env_enable_thresholds_true_env_var():
    os.environ["ENABLE_THRESHOLDS"] = "True"
    yield os.environ["ENABLE_THRESHOLDS"]


@pytest.fixture
def findings_response_with_data():
    yield {
        "count": 5,
        "next": "null",
        "previous": "null",
        "results": [
            {
                "id": 1,
                "tags": [],
                "request_response": {"req_resp": []},
                "accepted_risks": [],
                "push_to_jira": "false",
                "age": 1,
                "sla_days_remaining": 30,
                "finding_meta": [],
                "related_fields": "null",
                "jira_creation": "null",
                "jira_change": "null",
                "display_status": "Active",
                "finding_groups": [],
                "vulnerability_ids": [],
                "title": "example_title",
                "date": "2023-03-08",
                "sla_start_date": "null",
                "cwe": 0,
                "cvssv3": "null",
                "cvssv3_score": "null",
                "url": "null",
                "severity": "critical",
                "description": "example_description",
                "mitigation": "example_mitigation",
                "impact": "null",
                "steps_to_reproduce": "null",
                "severity_justification": "null",
                "references": "example_reference",
                "active": "true",
                "verified": "false",
                "false_p": "false",
                "duplicate": "false",
                "out_of_scope": "false",
                "risk_accepted": "false",
                "under_review": "false",
                "last_status_update": "2023-03-08T12:00:18.247419Z",
                "under_defect_review": "false",
                "is_mitigated": "false",
                "thread_id": 0,
                "mitigated": "null",
                "numerical_severity": "S1",
                "last_reviewed": "2023-03-08T12:00:16.433156Z",
                "param": "null",
                "payload": "null",
                "hash_code": "61148c6c4e744945c1e3bfc0a933b87166c2aaaebb3bc45d4b713cca0cf29736",
                "line": 30,
                "file_path": "file1.yaml",
                "component_name": "example_component",
                "component_version": "null",
                "static_finding": "true",
                "dynamic_finding": "false",
                "created": "2023-03-08T12:00:18.209670Z",
                "scanner_confidence": "null",
                "unique_id_from_tool": "null",
                "vuln_id_from_tool": "null",
                "sast_source_object": "null",
                "sast_sink_object": "null",
                "sast_source_line": "null",
                "sast_source_file_path": "null",
                "nb_occurences": 1,
                "publish_date": "null",
                "service": "null",
                "planned_remediation_date": "null",
                "test": 460,
                "duplicate_finding": "null",
                "review_requested_by": "null",
                "defect_review_requested_by": "null",
                "mitigated_by": "null",
                "reporter": 8,
                "last_reviewed_by": 8,
                "sonarqube_issue": "null",
                "endpoints": [],
                "reviewers": [],
                "notes": [],
                "files": [],
                "found_by": [98],
            },
            {
                "id": 2,
                "tags": [],
                "request_response": {"req_resp": []},
                "accepted_risks": [],
                "push_to_jira": "false",
                "age": 1,
                "sla_days_remaining": 30,
                "finding_meta": [],
                "related_fields": "null",
                "jira_creation": "null",
                "jira_change": "null",
                "display_status": "Active",
                "finding_groups": [],
                "vulnerability_ids": [],
                "title": "example_title",
                "date": "2023-03-08",
                "sla_start_date": "null",
                "cwe": 0,
                "cvssv3": "null",
                "cvssv3_score": "null",
                "url": "null",
                "severity": "high",
                "description": "example_description",
                "mitigation": "example_mitigation",
                "impact": "null",
                "steps_to_reproduce": "null",
                "severity_justification": "null",
                "references": "example_reference",
                "active": "true",
                "verified": "false",
                "false_p": "false",
                "duplicate": "false",
                "out_of_scope": "false",
                "risk_accepted": "false",
                "under_review": "false",
                "last_status_update": "2023-03-08T12:00:18.247419Z",
                "under_defect_review": "false",
                "is_mitigated": "false",
                "thread_id": 0,
                "mitigated": "null",
                "numerical_severity": "S1",
                "last_reviewed": "2023-03-08T12:00:16.433156Z",
                "param": "null",
                "payload": "null",
                "hash_code": "61148c6c4e744945c1e3bfc0a933b87166c2aaaebb3bc45d4b713cca0cf29736",
                "line": 30,
                "file_path": "file1.yaml",
                "component_name": "example_component",
                "component_version": "null",
                "static_finding": "true",
                "dynamic_finding": "false",
                "created": "2023-03-08T12:00:18.209670Z",
                "scanner_confidence": "null",
                "unique_id_from_tool": "null",
                "vuln_id_from_tool": "null",
                "sast_source_object": "null",
                "sast_sink_object": "null",
                "sast_source_line": "null",
                "sast_source_file_path": "null",
                "nb_occurences": 1,
                "publish_date": "null",
                "service": "null",
                "planned_remediation_date": "null",
                "test": 460,
                "duplicate_finding": "null",
                "review_requested_by": "null",
                "defect_review_requested_by": "null",
                "mitigated_by": "null",
                "reporter": 8,
                "last_reviewed_by": 8,
                "sonarqube_issue": "null",
                "endpoints": [],
                "reviewers": [],
                "notes": [],
                "files": [],
                "found_by": [98],
            },
            {
                "id": 3,
                "tags": [],
                "request_response": {"req_resp": []},
                "accepted_risks": [],
                "push_to_jira": "false",
                "age": 1,
                "sla_days_remaining": 30,
                "finding_meta": [],
                "related_fields": "null",
                "jira_creation": "null",
                "jira_change": "null",
                "display_status": "Active",
                "finding_groups": [],
                "vulnerability_ids": [],
                "title": "example_title",
                "date": "2023-03-08",
                "sla_start_date": "null",
                "cwe": 0,
                "cvssv3": "null",
                "cvssv3_score": "null",
                "url": "null",
                "severity": "medium",
                "description": "example_description",
                "mitigation": "example_mitigation",
                "impact": "null",
                "steps_to_reproduce": "null",
                "severity_justification": "null",
                "references": "example_reference",
                "active": "true",
                "verified": "false",
                "false_p": "false",
                "duplicate": "false",
                "out_of_scope": "false",
                "risk_accepted": "false",
                "under_review": "false",
                "last_status_update": "2023-03-08T12:00:18.247419Z",
                "under_defect_review": "false",
                "is_mitigated": "false",
                "thread_id": 0,
                "mitigated": "null",
                "numerical_severity": "S1",
                "last_reviewed": "2023-03-08T12:00:16.433156Z",
                "param": "null",
                "payload": "null",
                "hash_code": "61148c6c4e744945c1e3bfc0a933b87166c2aaaebb3bc45d4b713cca0cf29736",
                "line": 30,
                "file_path": "file1.yaml",
                "component_name": "example_component",
                "component_version": "null",
                "static_finding": "true",
                "dynamic_finding": "false",
                "created": "2023-03-08T12:00:18.209670Z",
                "scanner_confidence": "null",
                "unique_id_from_tool": "null",
                "vuln_id_from_tool": "null",
                "sast_source_object": "null",
                "sast_sink_object": "null",
                "sast_source_line": "null",
                "sast_source_file_path": "null",
                "nb_occurences": 1,
                "publish_date": "null",
                "service": "null",
                "planned_remediation_date": "null",
                "test": 460,
                "duplicate_finding": "null",
                "review_requested_by": "null",
                "defect_review_requested_by": "null",
                "mitigated_by": "null",
                "reporter": 8,
                "last_reviewed_by": 8,
                "sonarqube_issue": "null",
                "endpoints": [],
                "reviewers": [],
                "notes": [],
                "files": [],
                "found_by": [98],
            },
            {
                "id": 1,
                "tags": [],
                "request_response": {"req_resp": []},
                "accepted_risks": [],
                "push_to_jira": "false",
                "age": 1,
                "sla_days_remaining": 30,
                "finding_meta": [],
                "related_fields": "null",
                "jira_creation": "null",
                "jira_change": "null",
                "display_status": "Active",
                "finding_groups": [],
                "vulnerability_ids": [],
                "title": "example_title",
                "date": "2023-03-08",
                "sla_start_date": "null",
                "cwe": 0,
                "cvssv3": "null",
                "cvssv3_score": "null",
                "url": "null",
                "severity": "low",
                "description": "example_description",
                "mitigation": "example_mitigation",
                "impact": "null",
                "steps_to_reproduce": "null",
                "severity_justification": "null",
                "references": "example_reference",
                "active": "true",
                "verified": "false",
                "false_p": "false",
                "duplicate": "false",
                "out_of_scope": "false",
                "risk_accepted": "false",
                "under_review": "false",
                "last_status_update": "2023-03-08T12:00:18.247419Z",
                "under_defect_review": "false",
                "is_mitigated": "false",
                "thread_id": 0,
                "mitigated": "null",
                "numerical_severity": "S1",
                "last_reviewed": "2023-03-08T12:00:16.433156Z",
                "param": "null",
                "payload": "null",
                "hash_code": "61148c6c4e744945c1e3bfc0a933b87166c2aaaebb3bc45d4b713cca0cf29736",
                "line": 30,
                "file_path": "file1.yaml",
                "component_name": "example_component",
                "component_version": "null",
                "static_finding": "true",
                "dynamic_finding": "false",
                "created": "2023-03-08T12:00:18.209670Z",
                "scanner_confidence": "null",
                "unique_id_from_tool": "null",
                "vuln_id_from_tool": "null",
                "sast_source_object": "null",
                "sast_sink_object": "null",
                "sast_source_line": "null",
                "sast_source_file_path": "null",
                "nb_occurences": 1,
                "publish_date": "null",
                "service": "null",
                "planned_remediation_date": "null",
                "test": 460,
                "duplicate_finding": "null",
                "review_requested_by": "null",
                "defect_review_requested_by": "null",
                "mitigated_by": "null",
                "reporter": 8,
                "last_reviewed_by": 8,
                "sonarqube_issue": "null",
                "endpoints": [],
                "reviewers": [],
                "notes": [],
                "files": [],
                "found_by": [98],
            },
            {
                "id": 1,
                "tags": [],
                "request_response": {"req_resp": []},
                "accepted_risks": [],
                "push_to_jira": "false",
                "age": 1,
                "sla_days_remaining": 30,
                "finding_meta": [],
                "related_fields": "null",
                "jira_creation": "null",
                "jira_change": "null",
                "display_status": "Active",
                "finding_groups": [],
                "vulnerability_ids": [],
                "title": "example_title",
                "date": "2023-03-08",
                "sla_start_date": "null",
                "cwe": 0,
                "cvssv3": "null",
                "cvssv3_score": "null",
                "url": "null",
                "severity": "info",
                "description": "example_description",
                "mitigation": "example_mitigation",
                "impact": "null",
                "steps_to_reproduce": "null",
                "severity_justification": "null",
                "references": "example_reference",
                "active": "true",
                "verified": "false",
                "false_p": "false",
                "duplicate": "false",
                "out_of_scope": "false",
                "risk_accepted": "false",
                "under_review": "false",
                "last_status_update": "2023-03-08T12:00:18.247419Z",
                "under_defect_review": "false",
                "is_mitigated": "false",
                "thread_id": 0,
                "mitigated": "null",
                "numerical_severity": "S1",
                "last_reviewed": "2023-03-08T12:00:16.433156Z",
                "param": "null",
                "payload": "null",
                "hash_code": "61148c6c4e744945c1e3bfc0a933b87166c2aaaebb3bc45d4b713cca0cf29736",
                "line": 30,
                "file_path": "file1.yaml",
                "component_name": "example_component",
                "component_version": "null",
                "static_finding": "true",
                "dynamic_finding": "false",
                "created": "2023-03-08T12:00:18.209670Z",
                "scanner_confidence": "null",
                "unique_id_from_tool": "null",
                "vuln_id_from_tool": "null",
                "sast_source_object": "null",
                "sast_sink_object": "null",
                "sast_source_line": "null",
                "sast_source_file_path": "null",
                "nb_occurences": 1,
                "publish_date": "null",
                "service": "null",
                "planned_remediation_date": "null",
                "test": 460,
                "duplicate_finding": "null",
                "review_requested_by": "null",
                "defect_review_requested_by": "null",
                "mitigated_by": "null",
                "reporter": 8,
                "last_reviewed_by": 8,
                "sonarqube_issue": "null",
                "endpoints": [],
                "reviewers": [],
                "notes": [],
                "files": [],
                "found_by": [98],
            },
        ],
        "prefetch": {},
    }


def test_main_defaults(
    mocker,
    defect_dojo_url_env_var,
    defect_dojo_username_env_var,
    defect_dojo_password_env_var,
    defect_dojo_product_env_var,
    finding_response_data_no_findings,
):
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.retrieve_defectdojo_token",
        return_value="d11dc2d650168f488e6143b6fa428483fbc7de29",
    )
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.get_findings_count_defectdojo",
        return_value=0,
    )
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.get_findings_defectdojo",
        return_value=finding_response_data_no_findings,
    )
    mocker.patch(
        "defectdojo.src.active_findings.github_actions.set_action_outputs",
        return_value=None,
    )
    mocker.patch(
        "defectdojo.src.active_findings.github_actions.active_findings_markdown_step_summary",
        return_value=None,
    )
    result = active_findings.main()
    assert result is None


def test_main_failed_thresholds_false(
    mocker,
    defect_dojo_url_env_var,
    defect_dojo_username_env_var,
    defect_dojo_password_env_var,
    defect_dojo_product_env_var,
    env_create_github_outputs_false_env_var,
    env_create_github_step_summary_false_env_var,
    env_enable_thresholds_true_env_var,
    findings_response_with_data,
):
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.retrieve_defectdojo_token",
        return_value="d11dc2d650168f488e6143b6fa428483fbc7de29",
    )
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.get_findings_count_defectdojo",
        return_value=0,
    )
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.get_findings_defectdojo",
        return_value=findings_response_with_data,
    )
    mocker.patch(
        "defectdojo.src.active_findings.findings_thresholds.evaluate_thresholds",
        return_value=False,
    )
    result = active_findings.main()
    assert result is None


def test_main_failed_thresholds_true(
    mocker,
    defect_dojo_url_env_var,
    defect_dojo_username_env_var,
    defect_dojo_password_env_var,
    defect_dojo_product_env_var,
    env_create_github_outputs_false_env_var,
    env_create_github_step_summary_false_env_var,
    env_enable_thresholds_true_env_var,
    findings_response_with_data,
):
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.retrieve_defectdojo_token",
        return_value="d11dc2d650168f488e6143b6fa428483fbc7de29",
    )
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.get_findings_count_defectdojo",
        return_value=0,
    )
    mocker.patch(
        "defectdojo.src.active_findings.defectdojo_api.get_findings_defectdojo",
        return_value=findings_response_with_data,
    )
    mocker.patch(
        "defectdojo.src.active_findings.findings_thresholds.evaluate_thresholds",
        return_value=True,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        active_findings.main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

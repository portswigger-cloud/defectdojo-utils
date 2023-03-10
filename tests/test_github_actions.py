import os
import pytest
import github_actions


@pytest.fixture
def github_output_env_var(tmp_path) -> pytest.fixture():
    os.environ["GITHUB_OUTPUT"] = f"{tmp_path}/github_output"
    yield os.environ["GITHUB_OUTPUT"]


@pytest.fixture
def github_step_summary_env_var(tmp_path) -> pytest.fixture():
    os.environ["GITHUB_STEP_SUMMARY"] = f"{tmp_path}/github_step_summary"
    yield os.environ["GITHUB_STEP_SUMMARY"]


@pytest.fixture
def output_data():
    yield {
        "total": 10,
        "critical": 2,
        "high": 2,
        "medium": 2,
        "low": 2,
        "info": 2,
    }


@pytest.fixture
def set_summary_data(output_data):
    data = output_data.copy()
    data["product"] = "test_product"
    yield data


@pytest.fixture
def set_total_findings_threshold_data():
    yield {"active_finding": 15, "threshold": 10}


@pytest.fixture
def set_severity_findings_threshold_data(set_total_findings_threshold_data):
    data = set_total_findings_threshold_data.copy()
    data["severity"] = "critical"
    yield data


def test_set_action_outputs(tmpdir, github_output_env_var, output_data):
    file = tmpdir.join("github_output")
    github_actions.set_action_outputs(output_data)
    assert file.read() == "total=10\ncritical=2\nhigh=2\nmedium=2\nlow=2\ninfo=2\n"


def test_active_findings_markdown_step_summary(
    tmpdir, github_step_summary_env_var, set_summary_data
):
    file = tmpdir.join("github_step_summary")
    github_actions.active_findings_markdown_step_summary(**set_summary_data)
    assert (
        file.read()
        == "DefectDojo active findings summary for test_product\n* Total: 10\n* Critical: \
2\n* High: 2\n* Medium: 2\n* Low: 2\n* Info: 2\n\n"
    )


def test_total_findings_threshold_markdown_step_summary(
    tmpdir, github_step_summary_env_var, set_total_findings_threshold_data
):
    file = tmpdir.join("github_step_summary")
    github_actions.total_findings_threshold_markdown_step_summary(
        **set_total_findings_threshold_data
    )
    assert (
        file.read()
        == "The total number of security findings 15 is greater than the configured \
threshold of 10\n\n"
    )


def test_severity_findings_threshold_markdown_step_summary(
    tmpdir, github_step_summary_env_var, set_severity_findings_threshold_data
):
    file = tmpdir.join("github_step_summary")
    github_actions.severity_findings_threshold_markdown_step_summary(
        **set_severity_findings_threshold_data
    )
    assert (
        file.read()
        == "The number of critical security findings 15 is greater than the configured \
threshold of 10\n\n"
    )

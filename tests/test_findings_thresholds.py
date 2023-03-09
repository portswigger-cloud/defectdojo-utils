import pytest
import defectdojo.src.findings_thresholds as findings_thresholds


@pytest.fixture
def setup_active_findings():
    yield {
        "total": 10,
        "critical": 2,
        "high": 2,
        "medium": 2,
        "low": 2,
        "info": 2,
    }


@pytest.fixture
def setup_findings_thresholds_exceeded():
    yield {
        "total": 5,
        "critical": 1,
        "high": 1,
        "medium": 1,
        "low": 1,
        "info": 1,
    }


@pytest.fixture
def setup_findings_thresholds_not_exceeded():
    yield {
        "total": 20,
        "critical": 4,
        "high": 4,
        "medium": 4,
        "low": 4,
        "info": 4,
    }


def test_evaluate_thresholds_exceeded(
    mocker, setup_active_findings, setup_findings_thresholds_exceeded
):
    mocker.patch(
        "defectdojo.src.findings_thresholds.github_actions.total_findings_threshold_markdown_step_summary",
        return_value=None,
    )
    mocker.patch(
        "defectdojo.src.findings_thresholds.github_actions.total_findings_threshold_markdown_step_summary",
        return_value=None,
    )
    result = findings_thresholds.evaluate_thresholds(
        setup_active_findings, setup_findings_thresholds_exceeded
    )

    assert result is True


def test_evaluate_thresholds_not_exceeded(
    mocker, setup_active_findings, setup_findings_thresholds_not_exceeded
):
    mocker.patch(
        "defectdojo.src.findings_thresholds.github_actions.total_findings_threshold_markdown_step_summary",
        return_value=None,
    )
    mocker.patch(
        "defectdojo.src.findings_thresholds.github_actions.total_findings_threshold_markdown_step_summary",
        return_value=None,
    )
    result = findings_thresholds.evaluate_thresholds(
        setup_active_findings, setup_findings_thresholds_not_exceeded
    )

    assert result is False

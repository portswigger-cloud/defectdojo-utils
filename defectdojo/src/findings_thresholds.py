import defectdojo.src.github_actions as github_actions


def evaluate_thresholds(active_findings: dict, findings_thresholds: dict) -> bool:
    threshold_exceeded_count = 0
    if active_findings["total"] > findings_thresholds["total"]:
        github_actions.total_findings_threshold_markdown_step_summary(
            active_findings["total"], findings_thresholds["total"]
        )
        threshold_exceeded_count + 1

    if active_findings["critical"] > findings_thresholds["critical"]:
        github_actions.severity_findings_threshold_markdown_step_summary(
            "critical", active_findings["critical"], findings_thresholds["critical"]
        )
        threshold_exceeded_count + 1

    if active_findings["high"] > findings_thresholds["high"]:
        github_actions.severity_findings_threshold_markdown_step_summary(
            "high", active_findings["high"], findings_thresholds["high"]
        )
        threshold_exceeded_count + 1

    if active_findings["medium"] > findings_thresholds["medium"]:
        github_actions.severity_findings_threshold_markdown_step_summary(
            "medium", active_findings["medium"], findings_thresholds["medium"]
        )
        threshold_exceeded_count + 1

    if active_findings["low"] > findings_thresholds["low"]:
        github_actions.severity_findings_threshold_markdown_step_summary(
            "low", active_findings["low"], findings_thresholds["low"]
        )
        threshold_exceeded_count + 1

    if active_findings["info"] > findings_thresholds["info"]:
        github_actions.severity_findings_threshold_markdown_step_summary(
            "info", active_findings["info"], findings_thresholds["info"]
        )
        threshold_exceeded_count + 1
    if threshold_exceeded_count > 0:
        return True
    else:
        return False

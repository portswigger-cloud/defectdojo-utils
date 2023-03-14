import os

active_findings_markdown_summary_template = """DefectDojo active findings summary for {0}
* Total: {1}
* Critical: {2}
* High: {3}
* Medium: {4}
* Low: {5}
* Info: {6}
"""

total_findings_threshold_markdown_summary_template = """The total number of security findings {0} is greater than the configured threshold of {1}
"""

severity_findings_threshold_markdown_summary_template = """The number of {0} security findings {1} is greater than the configured threshold of {2}
"""


def set_action_outputs(output_pairs: dict):
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            for key, value in output_pairs.items():
                print("{0}={1}".format(key, value), file=f)


def active_findings_markdown_step_summary(
    product,
    total,
    critical,
    high,
    medium,
    low,
    info,
):
    if "GITHUB_STEP_SUMMARY" in os.environ:
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            print(
                active_findings_markdown_summary_template.format(
                    product,
                    total,
                    critical,
                    high,
                    medium,
                    low,
                    info,
                ),
                file=f,
            )


def total_findings_threshold_markdown_step_summary(active_finding, threshold):
    if "GITHUB_STEP_SUMMARY" in os.environ:
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            print(
                total_findings_threshold_markdown_summary_template.format(
                    active_finding,
                    threshold,
                ),
                file=f,
            )


def severity_findings_threshold_markdown_step_summary(
    severity, active_finding, threshold
):
    if "GITHUB_STEP_SUMMARY" in os.environ:
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            print(
                severity_findings_threshold_markdown_summary_template.format(
                    severity,
                    active_finding,
                    threshold,
                ),
                file=f,
            )

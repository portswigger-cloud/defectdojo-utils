import os


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
    active_findings_markdown_summary_template = """## DefectDojo Findings Summary
    ## {0} Findings Summary
    * __Total:__{1}
    * __Critical:__{2}
    * __High:__{3}
    * __Medium:__{4}
    * __Low:__{5}
    * __Info:__{6}
    * __Generated by:__ portswigger-cloud active-findings
    """

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
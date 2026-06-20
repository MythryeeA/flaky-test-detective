import os


def generate_issue(flaky_tests, root_causes):

    if not flaky_tests:
        return "No flaky tests detected."

    report = "# Flaky Test Investigation Report\n\n"

    for test, info in flaky_tests.items():

        report += f"## {test}\n\n"
        report += f"**History:** {info['history']}\n\n"
        report += f"**Instability Score:** {info['instability_score']}\n\n"
        report += f"**Probable Cause:** {root_causes[test]}\n\n"
        report += "---\n\n"

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/flaky_issue_report.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    return report
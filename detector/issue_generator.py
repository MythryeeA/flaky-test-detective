def generate_issue(flaky_tests, root_causes):

    if not flaky_tests:
        return "No flaky tests detected."

    report = "\n=== FLAKY TEST INVESTIGATION REPORT ===\n\n"

    for test, info in flaky_tests.items():

        report += f"Test: {test}\n"
        report += f"History: {info['history']}\n"
        report += f"Instability Score: {info['instability_score']}\n"
        report += f"Probable Cause: {root_causes[test]}\n"
        report += "-" * 40 + "\n"

    return report
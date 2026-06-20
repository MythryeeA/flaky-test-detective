def generate_issue(flaky_tests):

    if not flaky_tests:
        return "No flaky tests detected."

    report = "\n=== FLAKY TEST REPORT ===\n\n"

    for test, info in flaky_tests.items():

        report += f"Test: {test}\n"
        report += f"History: {info['history']}\n"
        report += f"Instability Score: {info['instability_score']}\n"
        report += "-" * 30 + "\n"

    return report
def analyze_root_cause(flaky_tests):

    root_causes = {}

    for test_name, info in flaky_tests.items():

        score = info["instability_score"]

        if score >= 0.6:
            cause = "High instability detected. Possible timing issue, race condition, or external dependency."
        elif score >= 0.3:
            cause = "Moderate instability detected. Possible environment inconsistency."
        else:
            cause = "Low instability detected. Requires further investigation."

        root_causes[test_name] = cause

    return root_causes
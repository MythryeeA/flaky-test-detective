from collections import defaultdict


def detect_flaky_tests(parsed_runs):
    history = defaultdict(list)

    for run in parsed_runs:
        for test, status in run.items():
            history[test].append(status)

    flaky_tests = {}

    for test, statuses in history.items():

        if "PASS" in statuses and "FAIL" in statuses:

            instability_score = statuses.count("FAIL") / len(statuses)

            flaky_tests[test] = {
                "history": statuses,
                "instability_score": round(instability_score, 2)
            }

    return flaky_tests
from collections import defaultdict


def detect_flaky_tests(parsed_runs):

    history = defaultdict(list)

    for run in parsed_runs:

        for test, details in run.items():

            history[test].append(details)

    flaky_tests = {}

    for test, records in history.items():

        statuses = [r["status"] for r in records]

        if "PASS" in statuses and "FAIL" in statuses:

            instability_score = statuses.count("FAIL") / len(statuses)

            flaky_tests[test] = {
                "history": statuses,
                "records": records,
                "instability_score": round(instability_score, 2)
            }

    return flaky_tests
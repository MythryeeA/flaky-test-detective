from collections import Counter


def analyze_root_cause(flaky_tests):

    root_causes = {}

    for test_name, info in flaky_tests.items():

        errors = []

        for record in info["records"]:

            if record["status"] == "FAIL":
                errors.append(record["error"])

        if errors:

            common_error = Counter(errors).most_common(1)[0][0]

            root_causes[test_name] = (
                f"Repeated failure pattern detected. "
                f"Most common error: {common_error}"
            )

        else:

            root_causes[test_name] = (
                "Insufficient evidence. Further investigation required."
            )

    return root_causes
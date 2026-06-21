def evaluate_flakiness(history):

    statuses = [
        run["status"]
        for run in history
    ]

    failures = statuses.count("failure")

    total = len(statuses)

    instability_score = failures / total

    if (
        failures > 0
        and failures < total
    ):
        verdict = "LIKELY_FLAKY"

        recommendation = (
            "Investigate and monitor"
        )

    elif failures == total:

        verdict = "CONSISTENT_FAILURE"

        recommendation = (
            "Treat as genuine defect"
        )

    else:

        verdict = "STABLE"

        recommendation = (
            "No action required"
        )

    return {
        "instability_score":
            round(instability_score, 2),

        "verdict":
            verdict,

        "recommendation":
            recommendation
    }
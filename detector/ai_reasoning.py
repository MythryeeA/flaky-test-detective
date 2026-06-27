def generate_ai_summary(history, decision):

    total = len(history)

    failures = sum(
        1 for run in history
        if run["status"] == "failure"
    )

    successes = total - failures

    confidence = round(
        (1 - decision["instability_score"]) * 100,
        1
    )

    summary = f"""
### AI Investigation Summary

The agent analyzed the most recent {total} GitHub workflow executions.

Results:
• Successful runs: {successes}
• Failed runs: {failures}

The workflow history contains both successful and failed executions,
indicating intermittent behaviour rather than a persistent software defect.

Based on this evidence, the agent classified the repository as:

{decision["verdict"]}

Possible causes include:

• Timing issues
• External dependency instability
• Network/API timeout
• Resource contention

Recommended Action:

Continue monitoring future executions before disabling or quarantining the test.

Confidence: {confidence}%
"""

    return summary, confidence
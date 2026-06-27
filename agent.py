from agent_brain import AgentBrain


def investigate():

    brain = AgentBrain()

    history = brain.observe()

    decision = brain.reason()

    plan = brain.plan_action()

    issue = brain.act()

    failures = sum(
        1 for run in history
        if run["status"] == "failure"
    )

    confidence = round(
        (1 - decision["instability_score"]) * 100,
        1
    )

    report = f"""
Repository: flaky-test-lab

Workflow Runs: {len(history)}

Failures: {failures}

Verdict: {decision["verdict"]}

Action: {plan["action"]}
"""

    return {

        "history": history,

        "decision": decision,

        "plan": plan,

        "failures": failures,

        "confidence": confidence,

        "llm_summary": brain.llm_summary,

        "report": report,

        "issue_url": issue

    }
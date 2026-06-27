from detector.github_workflow_reader import get_workflow_history
from detector.flakiness_decision_engine import evaluate_flakiness
from detector.llm_reasoner import investigate_with_llm
from detector.github_issue_creator import create_github_issue


class AgentBrain:

    def __init__(self):

        self.observation = None
        self.decision = None
        self.llm_summary = None
        self.plan = None

    # ----------------------
    # Observe
    # ----------------------

    def observe(self):

        history = get_workflow_history()

        self.observation = history

        return history

    # ----------------------
    # Reason
    # ----------------------

    def reason(self):

        self.decision = evaluate_flakiness(
            self.observation
        )

        self.llm_summary = investigate_with_llm(
            self.observation,
            self.decision
        )

        return self.decision

    # ----------------------
    # Plan
    # ----------------------

    def plan_action(self):

        if self.decision["verdict"] == "LIKELY_FLAKY":

            self.plan = {
                "action": "CREATE_GITHUB_ISSUE",
                "priority": "MEDIUM",
                "human_review": True
            }

        else:

            self.plan = {
                "action": "NO_ACTION",
                "priority": "LOW",
                "human_review": False
            }

        return self.plan

    # ----------------------
    # Act
    # ----------------------

    def act(self):

        issue = None

        if self.plan["action"] == "CREATE_GITHUB_ISSUE":

            issue = create_github_issue(

                "Flaky Workflow Investigation",

                self.llm_summary

            )

        return issue
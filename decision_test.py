from detector.github_workflow_reader import (
    get_workflow_history
)

from detector.flakiness_decision_engine import (
    evaluate_flakiness
)

history = get_workflow_history()

decision = evaluate_flakiness(
    history
)

print(decision)
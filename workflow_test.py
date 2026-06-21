from detector.github_workflow_reader import get_workflow_history

history = get_workflow_history()

for run in history:
    print(run)
from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

def get_workflow_history():

    token = os.getenv("GITHUB_TOKEN")

    github = Github(token)

    repo = github.get_repo(
        "MythryeeA/flaky-test-lab"
    )

    runs = repo.get_workflow_runs()

    history = []

    for run in runs[:10]:

        history.append({
            "name": run.name,
            "status": run.conclusion
        })

    return history
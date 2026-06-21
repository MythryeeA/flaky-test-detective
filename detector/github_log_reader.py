from github import Github
from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_latest_failed_run_logs():

    token = os.getenv("GITHUB_TOKEN")

    github = Github(token)

    repo = github.get_repo(
        "MythryeeA/flaky-test-lab"
    )

    runs = repo.get_workflow_runs()

    for run in runs:

        if run.conclusion == "failure":

            return {
                "run_id": run.id,
                "html_url": run.html_url
            }

    return None
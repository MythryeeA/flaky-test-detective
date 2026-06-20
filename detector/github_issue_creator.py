from github import Github
from dotenv import load_dotenv
import os


load_dotenv()


def create_github_issue(title, body):

    token = os.getenv("GITHUB_TOKEN")

    github = Github(token)

    repo = github.get_repo(
        "MythryeeA/flaky-test-detective"
    )

    issue = repo.create_issue(
        title=title,
        body=body
    )

    return issue.html_url
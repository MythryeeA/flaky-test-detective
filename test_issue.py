from detector.github_issue_creator import create_github_issue


url = create_github_issue(
    "Test Issue From Agent",
    "This issue was generated automatically."
)

print(url)
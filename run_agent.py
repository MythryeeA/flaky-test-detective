from agent import investigate


print("\n=== FLAKY TEST DETECTIVE ===\n")

result = investigate()

print(result["report"])

if result["issue_url"]:

    print("\nGitHub Issue Created:")
    print(result["issue_url"])
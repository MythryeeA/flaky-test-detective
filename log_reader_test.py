from detector.github_log_reader import (
    get_latest_failed_run_logs
)

result = get_latest_failed_run_logs()

print(result)
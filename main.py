from detector.log_parser import parse_log
from detector.flake_detector import detect_flaky_tests
from detector.issue_generator import generate_issue


logs = [
    "sample_logs/run1.log",
    "sample_logs/run2.log",
    "sample_logs/run3.log"
]

parsed_runs = []

for log in logs:
    parsed_runs.append(parse_log(log))

flaky_tests = detect_flaky_tests(parsed_runs)

report = generate_issue(flaky_tests)

print(report)
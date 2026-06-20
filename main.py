from detector.log_parser import parse_log
from detector.flake_detector import detect_flaky_tests
from detector.root_cause_analyzer import analyze_root_cause
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

root_causes = analyze_root_cause(flaky_tests)

report = generate_issue(
    flaky_tests,
    root_causes
)

print(report)
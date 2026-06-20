def parse_log(file_path):
    tests = {}

    with open(file_path, "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        if i + 1 < len(lines):
            test_name = lines[i].split(":")[1].strip()
            status = lines[i + 1].split(":")[1].strip()

            tests[test_name] = status

    return tests
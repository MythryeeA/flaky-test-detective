def parse_log(file_path):

    tests = {}

    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    for i in range(0, len(lines), 4):

        test_name = lines[i].split(":")[1].strip()
        status = lines[i + 1].split(":")[1].strip()
        error = lines[i + 2].split(":")[1].strip()
        duration = int(lines[i + 3].split(":")[1].strip())

        tests[test_name] = {
            "status": status,
            "error": error,
            "duration": duration
        }

    return tests
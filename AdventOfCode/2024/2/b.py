input = "./input"

def is_safe(report):
    is_safe = is_safe_helper(report)
    if is_safe:
        return True
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe_helper(modified_report):
                return True
    return False

def is_safe_helper(report):
    trend = None
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if trend is None:
            if diff in (1, 2, 3):
                trend = (1, 2, 3)
            elif diff in (-1, -2, -3):
                trend = (-1, -2, -3)
            else:
                return False
        else:
            if diff not in trend:
                return False
    return True

reports = []

with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        reports.append([int(x) for x in line.strip().split()])

safety_dict = {}

for report in reports:
    if is_safe(report):
        safety_dict["safe"] = safety_dict.get("safe", 0) + 1
    else:
        safety_dict["unsafe"] = safety_dict.get("unsafe", 0) + 1
print(f"Safe reports: {safety_dict['safe']} Unsafe reports: {safety_dict['unsafe']}")
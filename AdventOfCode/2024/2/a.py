input = "./input"

reports = []

with open(input, "r") as file:
    lines = file.readlines()
    for line in lines:
        reports.append([int(x) for x in line.strip().split()])

safety_dict = {"safe": 0, "unsafe": 0}

for report in reports:
    trend = None
    safe = True
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if trend is None:
            if diff in (1, 2, 3):
                trend = (1, 2, 3)
            elif diff in (-1, -2, -3):
                trend = (-1, -2, -3)
            else:
                safe = False
                break
        else:
            if diff in trend:
                continue
            else:
                safe = False
                break
    safety_dict["safe" if safe else "unsafe"] += 1
print(f"Safe reports: {safety_dict['safe']} Unsafe reports: {safety_dict['unsafe']}")
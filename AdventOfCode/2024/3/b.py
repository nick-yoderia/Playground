import re

input = "./input"
with open(input, "r") as file:
    text = file.read()

pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"

match = re.findall(pattern, text)

pattern = r"\d+"
sum = 0
do_flag = True
if match:
    for m in match:
        if m == "do()":
            do_flag = True
            continue
        elif m == "don't()":
            do_flag = False
            continue
        elif m.startswith("mul(") and do_flag:
            m = m[4:-1]
            a = [int(x) for x in m.split(",")]
            sum += a[0] * a[1]

print(sum)
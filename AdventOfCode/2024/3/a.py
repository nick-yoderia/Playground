import re

input = "./input"
with open(input, "r") as file:
    text = file.read()

pattern = r"mul\(\d+,\d+\)"

match = re.findall(pattern, text)

pattern = r"\d+"
sum = 0
if match:
    for m in match:
        a = [int(x) for x in re.findall(pattern, m)]
        sum += a[0] * a[1]

print(sum)
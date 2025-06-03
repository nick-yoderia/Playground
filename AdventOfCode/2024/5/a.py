import re

input = "./input"

with open(input, "r") as file:
    lines = file.readlines()

rules = [line.strip() for line in lines if "|" in line]
rules_dict = {}
for rule in rules:
    rule = rule.split("|")
    key = int(rule[0])
    rules_dict.setdefault(key, []).append(int(rule[1].strip()))

updates = [line.strip() for line in lines if "," in line]
updates = [[int(nums) for nums in re.findall(r'\d+', update)] for update in updates]

valid_updates = []
for update in updates:
    previous = set()
    valid = True
    for num in update:
        if num in rules_dict:
            rules_for_num = rules_dict[num]
            for rule_check in rules_for_num:
                if rule_check in previous:
                    valid = False
                    break
        previous.add(num)
    if valid: valid_updates.append(update)

sum = 0
for valid in valid_updates:
    sum += valid[int(len(valid)/2)]

print(sum)
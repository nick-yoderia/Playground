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

# Converts an update to a valid update if it is not already valid.
def valid(update, rules_dict):
    previous = set()
    for i in range(len(update)):
        if update[i] in rules_dict:
            rules_for_current = rules_dict[update[i]]
            for rule in rules_for_current:
                if rule in previous:
                    update[i-1], update[i] = update[i], update[i-1]
                    return valid(update, rules_dict)
        previous.add(update[i])
    return update

# Returns update if it is invalid.
def get_invalid(update, rules_dict):
    previous = set()
    for num in update:
        if num in rules_dict:
            rules_for_current = rules_dict[num]
            for rule in rules_for_current:
                if rule in previous:
                    return update
        previous.add(num)

invalid_updates = [get_invalid(v, rules_dict) for v in updates]
invalid_converted = [valid(v, rules_dict) for v in invalid_updates if v is not None]
    
sum = 0
for valid_update in invalid_converted:
    sum += valid_update[int(len(valid_update)/2)]

print(sum)
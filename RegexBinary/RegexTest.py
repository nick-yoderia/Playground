import re

regex = r'^((0*)|(11)*|(10(1|(00))*01))*$'
multiple = 3

for i in range(1000001):
    binary = bin(i)[2:]
    match = re.match(regex, binary)
    if match:
        if not (i % multiple == 0):
            print(f"{i} matched but should not have")
    else:
        if i % multiple == 0:
            print(f"{i} did not match but should have")
print("If nothing printed, the regex is correct.")

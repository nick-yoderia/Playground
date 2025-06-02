import re

def search(input):
    found = 0
    for s in input:
        found += len(re.findall(r"xmas", s))
        found += len(re.findall(r"samx", s))
    return found

input = "./input"
with open(input, "r") as file:
    text = file.read().lower()
    rows = text.splitlines()


columns = [""] * len(rows[0])
for i in range(len(rows[0])):
    for row in rows:
        columns[i] += row[i]

# Diagonals: top-left to bottom-right
diagonals1 = [""] * (len(rows) + len(columns) - 1)
for i in range(len(rows)):
    for j in range(len(columns)):
        diagonals1[i + j] += rows[i][j]
        
# Diagonals: top-right to bottom-left
diagonals2 = [""] * (len(rows) + len(columns) - 1)
for i in range(len(rows)):
    for j in range(len(columns)):
        diagonals2[i - j + len(columns) - 1] += rows[i][j]

sum_xmax = (search(rows) + search(columns) + search(diagonals1) + search(diagonals2))
print(f"Total occurrences of 'xmas' or 'samx': {sum_xmax}")
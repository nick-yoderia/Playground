input = "./input"
with open(input, "r") as file:
    text = file.read().lower()
    line_width = len(text.splitlines()[0])
    text = text.replace("\n", "")

positions_of_a = [i for i, c in enumerate(text) if c == 'a']

total_crosses = 0
for i in positions_of_a:
    valid = ("mas", "sam")
    # Check if we are near an edge
    if i < line_width or i >= len(text) - line_width \
    or i % line_width == 0 or (i + 1) % line_width == 0:
        continue
    diagonal1 = text[i - line_width - 1] + text[i] + text[i + line_width + 1]
    diagonal2 = text[i - line_width + 1] + text[i] + text[i + line_width - 1]

    if diagonal1 in valid and diagonal2 in valid:
        total_crosses += 1
print(f"Total occurrences of 'xmas' or 'samx': {total_crosses}")
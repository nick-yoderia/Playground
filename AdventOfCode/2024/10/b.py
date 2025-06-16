def load_data(input):
    with open (input, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        data = [[int(char) if char != '.' else None for char in line] for line in data]
    return data

def count_paths(data):
    trail_heads = []
    for y, line in enumerate(data):
        for x, height in enumerate(line):
            if height == 0:
                trail_heads.append(count_paths_helper(data, y, x))
    return trail_heads

def count_paths_helper(data, y, x):
    if data[y][x] == 9:
        return 1
    total = 0
    if y - 1 >= 0 and data[y-1][x] == data[y][x] + 1:
        total += count_paths_helper(data, y-1, x)
    if y + 1 < len(data) and data[y+1][x] == data[y][x] + 1:
        total += count_paths_helper(data, y+1, x)
    if x - 1 >= 0 and data[y][x-1] == data[y][x] + 1:
        total += count_paths_helper(data, y, x-1)
    if x + 1 < len(data[y]) and data[y][x+1] == data[y][x] + 1:
        total += count_paths_helper(data, y, x+1)
    return total

if __name__ == '__main__':
    data = load_data('input')
    paths = count_paths(data)
    print(sum(paths))
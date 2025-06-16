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
                valid_paths = [0]
                count_paths_helper(data, y, x, valid_paths)
                trail_heads.append(valid_paths[0])
    return trail_heads

def count_paths_helper(data, y, x, valid_paths):
    if data[y][x] == 9:
        valid_paths[0] += 1
    if y - 1 != None and y - 1 >= 0 and data[y-1][x] == data[y][x] + 1:
        count_paths_helper(data, y-1, x, valid_paths)
    if y + 1 != None and y + 1 < len(data) and data[y+1][x] == data[y][x] + 1:
        count_paths_helper(data, y+1, x, valid_paths)
    if x - 1 != None and x - 1 >= 0 and data[y][x-1] == data[y][x] + 1:
        count_paths_helper(data, y, x-1, valid_paths)
    if x + 1 != None and x + 1 < len(data[y]) and data[y][x+1] == data[y][x] + 1:
        count_paths_helper(data, y, x+1, valid_paths)

if __name__ == '__main__':
    data = load_data('input')
    paths = count_paths(data)
    print(sum(paths))
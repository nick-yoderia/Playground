import time 

def load_data(input):
    with open (input, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data

def find_boxes(data):
    visited = set()
    fences_count = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (y, x) not in visited:
                planters = set()
                current_fences = make_box(data, y, x, char, planters)
                fences_count += current_fences * len(planters)
                visited.update(planters)
    return fences_count

def make_box(data, y, x, char, planters: set):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]) or data[y][x] != char:
        return 1
    if (y, x) in planters:
        return 0
    planters.add((y, x))
    count = 0
    count += make_box(data, y-1, x, char, planters)
    count += make_box(data, y+1, x, char, planters)
    count += make_box(data, y, x-1, char, planters)
    count += make_box(data, y, x+1, char, planters)
    return count

if __name__ == '__main__':
    start_time = time.perf_counter()
    data = load_data('input')
    fences = find_boxes(data)
    end_time = time.perf_counter()
    print(fences)
    print(f"Runtime: {end_time-start_time:f} seconds")
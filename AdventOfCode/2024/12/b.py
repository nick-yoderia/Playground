import time

def load_data(input):
    with open (input, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data

def find_boxes(data):
    visited = set()
    sides_count = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (y, x) not in visited:
                planters = set()
                fences = set()
                make_box(data, y, x, char, planters, fences)
                sides_count += find_sides(fences, planters) * len(planters)
                visited.update(planters)
    return sides_count

def make_box(data, y, x, char, planters: set, fences: set):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]) or data[y][x] != char:
        fences.add((y, x))
        return
    if (y, x) in planters:
        return
    planters.add((y, x))
    make_box(data, y-1, x, char, planters, fences)
    make_box(data, y+1, x, char, planters, fences)
    make_box(data, y, x-1, char, planters, fences)
    make_box(data, y, x+1, char, planters, fences)
            
def find_sides(fences: set, planters: set):
    sides = 0
    visited = set()
    for y, x in fences:
        if (y+1, x) in fences or (y-1, x) in fences:
            sides += find_sides_helper(y, x, 1, 0, fences, visited)
        elif (y, x+1) in fences or (y, x-1) in fences:
            sides += find_sides_helper(y, x, 0, 1, fences, visited)
        else:
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if (y+dy, x+dx) in planters:
                    sides += 1
        print(visited)
    print(sides)
    return sides

def find_sides_helper(y, x, dy, dx, fences: list, visited: set):
    if (y, x) in fences and (y, x, dy, dx) not in visited:
        visited.add((y, x, dy, dx))
        find_sides_helper(y+dy, x+dx, dy, dx, fences, visited)
        find_sides_helper(y-dy, x-dx, dy, dx, fences, visited)
        return 1
    return 0

if __name__ == '__main__':
    start_time = time.perf_counter()
    data = load_data('input')
    fences = find_boxes(data)
    end_time = time.perf_counter()
    print(fences)
    print(f"Runtime: {end_time-start_time:f} seconds")
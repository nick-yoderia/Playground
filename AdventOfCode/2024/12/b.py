import time

def load_data(input):
    with open (input, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data

def find_boxes(data):
    visited = set()
    price = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (y, x) not in visited:
                planters = set()
                fences = set()
                this_price = 0
                make_box(data, y, x, char, planters, fences)
                sides = find_sides(planters, fences)
                this_price += sides * len(planters)
                #print(f"Region {char} has price {len(planters)} * {sides} = {this_price}")
                price += this_price
                visited.update(planters)
    return price

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

def find_sides(planters: set, fences: set):
    sum = 0
    while fences:
        y, x = list(fences)[0]
        visited = set()
        if (y+1, x) in planters:
            sum += walk_sides(y, x, 0, 1, planters, visited)
        elif (y-1, x) in planters:
            sum += walk_sides(y, x, 0, -1, planters, visited)
        elif (y, x+1) in planters:
            sum += walk_sides(y, x, -1, 0, planters, visited)
        elif (y, x-1) in planters:
            sum += walk_sides(y, x, 1, 0, planters, visited)
        visited = set((y, x) for y, x, _, _ in visited)
        fences = fences - visited
    return sum

def walk_sides(y, x, dy, dx, planters, visited: set):
    # base case: if we've already visited this edge with this direction, stop
    if (y, x, dy, dx) in visited:
        return 0
    visited.add((y, x, dy, dx))
    # if the cell to the right is not a planter, turn right and move forward 1
    if (y+dx, x-dy) not in planters:
        # turn right: (dy, dx) -> (dx, -dy)
        return 1 + walk_sides(y+dx, x-dy, dx, -dy, planters, visited)
    # if the next cell in the current direction is a planter, turn left
    elif (y+dy, x+dx) in planters:
        # turn left: (dy, dx) -> (-dx, dy)
        return 1 + walk_sides(y, x, -dx, dy, planters, visited)
    else:
        # move forward
        return walk_sides(y+dy, x+dx, dy, dx, planters, visited)

if __name__ == '__main__':
    start_time = time.perf_counter()
    data = load_data('input')
    fences = find_boxes(data)
    end_time = time.perf_counter()
    print(fences)
    print(f"Runtime: {end_time-start_time:f} seconds")
input = "./input.txt"

with open(input, 'r') as file:
    map = file.readlines()
    map = [list(line.strip()) for line in map]

obstruction = '#'
guard = ('^', '>', 'v', '<')
visited = 'X'

def get_guard_pos(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] in guard:
                return (x, y, map[x][y])

def move_guard(guard_info, map):
    x, y = guard_info[0], guard_info[1]
    guard = guard_info[2]
    if guard == '^' and x > 0:
        if map[x-1][y] != obstruction:
            map[x-1][y] = '^'
            map[x][y] = 'X'
            return (x-1, y, guard), map
        else:
            map[x][y] = '>'
            return (x, y, '>'), map
    elif guard == '>' and y < len(map[0]) - 1:
        if map[x][y+1] != obstruction:
            map[x][y+1] = '>'
            map[x][y] = 'X'
            return (x, y+1, guard), map
        else:
            map[x][y] = 'v'
            return (x, y, 'v'), map
    elif guard == 'v' and x < len(map) - 1:
        if map[x+1][y] != obstruction:
            map[x+1][y] = 'v'
            map[x][y] = 'X'
            return (x+1, y, guard), map
        else:
            map[x][y] = '<'
            return (x, y, '<'), map
    elif guard == '<' and y > 0:
        if map[x][y-1] != obstruction:
            map[x][y-1] = '<'
            map[x][y] = 'X'
            return (x, y-1, guard), map
        else:
            map[x][y] = '^'
            return (x, y, '^'), map
    else:
        map[x][y] = 'X'
        return None, map

def count_visited(map):
    sum = 0
    for row in map:
        for pos in row:
            if pos == visited: sum +=1
    return sum

guard = get_guard_pos(map)

while guard is not None:
    guard, map = move_guard(guard, map)

print(count_visited(map))

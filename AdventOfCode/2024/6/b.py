input = "./input.txt"
obstruction = '#'
guard_states = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
visited = 'X'

with open(input, 'r') as file:
    map = file.readlines()
    map = [list(line.strip()) for line in map]
    maxx, maxy = len(map), len(map[0])
    obs_positions = set()
    empty_spaces = set()
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] in obstruction:
                obs_positions.add((x, y))
            elif map[x][y] in guard_states:
                guard_pos = (x, y)
                guard_direction = guard_states[map[x][y]]
            else:
                empty_spaces.add((x, y))

# given a 2d velocity vector rotate 90 degrees clockwise
def turn_right(guard_direction):
    return (guard_direction[1], -guard_direction[0])

def get_visited(guard_direction, guard_pos, maxx, maxy, obs_positions):
    visited = set()
    x = guard_pos[0]
    y = guard_pos[1]
    while x >= 0 and x < maxx and y >= 0 and y < maxy:
        next_pos = tuple(x + y for x, y in zip((x, y), guard_direction))
        if next_pos not in obs_positions:
            visited.add((x, y))
            x, y = next_pos[0], next_pos[1]
        else:
            guard_direction = turn_right(guard_direction)
    return visited

def is_a_loop(guard_direction, guard_pos, maxx, maxy, obs_positions):
    visited = set()
    x = guard_pos[0]
    y = guard_pos[1]
    loop_start = (x, y), guard_direction
    loop_found = False
    while x >= 0 and x < maxx and y >= 0 and y < maxy and not loop_found:
        next_pos = tuple(x + y for x, y in zip((x, y), guard_direction))
        if (next_pos, guard_direction) == loop_start:
            loop_found = True
        elif next_pos not in obs_positions:
            visited.add((x, y))
            x, y = next_pos[0], next_pos[1]
            if next_pos not in visited:
                loop_start = next_pos, guard_direction
        else:
            guard_direction = turn_right(guard_direction)
    return loop_found

if __name__ == "__main__":
    # get visited to try each pos as a wall
    visited = get_visited(guard_direction, guard_pos, maxx, maxy, obs_positions)

    loop_count = 0
    for cord in visited:
        test_obs_positions = obs_positions.copy()
        test_obs_positions.add(cord)
        if is_a_loop(guard_direction, guard_pos, maxx, maxy, test_obs_positions): loop_count += 1
    print(loop_count)
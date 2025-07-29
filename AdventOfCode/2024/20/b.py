from collections import defaultdict
import time

def load_data(input):
    with open(input, 'r') as file:
        maze = file.read()
        maze = maze.splitlines()
        maze = [line.strip() for line in maze]
        maxy, maxx = len(maze), len(maze[0])
    return maze, maxy, maxx

def mapify(maze):
    tiles = set()
    for y in range(MAXY):
        for x in range(MAXX):
            if maze[y][x] == '.':
                tiles.add((y,x))
            elif maze[y][x] == 'S':
                tiles.add((y,x))
                start = (y, x)
            elif maze[y][x] == 'E':
                tiles.add((y,x))
                finish = (y, x)
    return tiles, start, finish

def find_path(tiles, start):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    path = {}
    visited = set()
    i = 1
    y, x = start
    while len(path) < len(tiles):
        visited.add((y,x))
        path[(y,x)] = len(tiles)-i
        for dy, dx in directions:
            new_y, new_x = y+dy, x+dx
            if (new_y, new_x) in tiles and (new_y, new_x) not in visited:
                y, x = new_y, new_x
                i+=1
                break
    return path

def draw_circle(point, radius):
    y0, x0 = point
    points = set()
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            if abs(dy) + abs(dx) <= radius:
                y, x = y0 + dy, x0 + dx
                points.add(((y, x), abs(dy) + abs(dx)))
    return points

def find_time_saves(path, cheat_length):
    saves = defaultdict(int)
    for start_tile in path:
        circle_points = draw_circle(start_tile, cheat_length)
        for end_tile, cheat_cost in circle_points:
            if end_tile in path:
                if path[end_tile] < path[start_tile]:
                    save = path[start_tile] - path[end_tile] - cheat_cost
                    if save > 0:
                        saves[save] += 1
    return saves

if __name__ == '__main__':
    start_time = time.perf_counter()
    track, MAXY, MAXX = load_data('input')
    tiles, start, finish = mapify(track)
    path = find_path(tiles, start)
    saves = find_time_saves(path, 20)

    total = 0
    for key in saves:
        if key >= 100:
            total += saves[key]
    print(total)

    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")
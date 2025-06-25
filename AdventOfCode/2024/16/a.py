import math
from functools import lru_cache

def load_data(input):
    with open(input, 'r') as file:
        maze = file.read()
        maze = maze.splitlines()
        maze = [line.strip() for line in maze]
        MAXY, MAXX = len(maze), len(maze[0])
    return maze, MAXY, MAXX

def mapify(maze):
    tiles = set()
    for y in range(MAXY):
        for x in range(MAXX):
            if maze[y][x] == '.':
                tiles.add((y,x))
            elif maze[y][x] == 'S':
                tiles.add((y,x))
                reindeer = (y, x)
            elif maze[y][x] == 'E':
                tiles.add((y,x))
                finish = (y, x)
    return tiles, reindeer, finish

def turn_right(direction):
    dy, dx = direction
    return dx, -dy

def turn_left(direction):
    dy, dx = direction
    return -dx, dy

def shortest_path(reindeer, direction, finish, tiles: set, visited: set):
    if reindeer == finish:
        return 0
    y, x = reindeer
    visited = visited | {(reindeer, direction)}
    shortest = [math.inf]

    dy, dx = direction
    next_pos = (y + dy, x + dx)
    if next_pos in tiles and (next_pos, (dy, dx)) not in visited:
        shortest.append(1 + shortest_path(next_pos, direction, finish, tiles, visited))

    dy, dx = turn_right(direction)
    next_pos = (y + dy, x + dx)
    if next_pos in tiles and (next_pos, (dy, dx)) not in visited:
        shortest.append(1001 + shortest_path(next_pos, (dy, dx), finish, tiles, visited))

    dy, dx = turn_left(direction)
    next_pos = (y + dy, x + dx)
    if next_pos in tiles and (next_pos, (dy, dx)) not in visited:
        shortest.append(1001 + shortest_path(next_pos, (dy, dx), finish, tiles, visited))

    path = min(shortest)
    return path
    

if __name__ == '__main__':
    DEBUG = True
    maze, MAXY, MAXX = load_data('input')
    tiles, reindeer, finish = mapify(maze)
    shortest = shortest_path(reindeer, (0,1), finish, tiles, set())
    print(shortest)
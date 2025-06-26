import math
import heapq
from collections import defaultdict

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

def shortest_path(reindeer, direction, finish, tiles:set):
    visited = defaultdict(lambda: math.inf)
    min_pq = []
    heapq.heappush(min_pq, (0, (reindeer, direction)))

    while min_pq:
        cost, previous = heapq.heappop(min_pq)
        pos, direction = previous
        visited[previous] = cost

        if pos == finish:
            return cost

        straight = tuple(map(sum, zip(pos, direction)))
        if straight in tiles and cost + 1 < visited[(straight, direction)]:
            visited[(straight, direction)] = cost + 1
            heapq.heappush(min_pq, (cost + 1, (straight, direction)))

        right_turn = turn_right(direction)
        if cost + 1000 < visited[(pos, right_turn)]:
            visited[(pos, right_turn)] = cost + 1000
            heapq.heappush(min_pq, (cost + 1000, (pos, right_turn)))

        left_turn = turn_left(direction)
        if cost + 1000 < visited[(pos, left_turn)]:
            visited[(pos, left_turn)] = cost + 1000
            heapq.heappush(min_pq, (cost + 1000, (pos, left_turn)))
        
    

if __name__ == '__main__':
    DEBUG = True
    maze, MAXY, MAXX = load_data('input')
    tiles, reindeer, finish = mapify(maze)
    shortest = shortest_path(reindeer, (0,1), finish, tiles)
    print(shortest)
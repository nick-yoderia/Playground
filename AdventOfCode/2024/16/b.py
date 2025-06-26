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

def find_optimal_tiles(visited_parent: dict, start, end, optimal_tiles: set):
    if start[0] == end:
        return
    for parent in visited_parent[start]:
        optimal_tiles.add(parent[0])
        find_optimal_tiles(visited_parent, parent, end, optimal_tiles)

def shortest_path(reindeer, direction, finish, tiles:set):
    visited_cost = defaultdict(lambda: math.inf)
    visited_parent = defaultdict(lambda: [])
    min_pq = []
    min_cost = 0
    heapq.heappush(min_pq, (0, (reindeer, direction)))

    while min_pq:
        cost, current = heapq.heappop(min_pq)
        pos, direction = current

        #Found shortest path
        if pos == finish:
            min_cost = cost
            break
        
        #Process for going straight
        straight = tuple(map(sum, zip(pos, direction)))
        if cost + 1 == visited_cost[(straight, direction)]:
            visited_parent[(straight, direction)].append((current))
        if straight in tiles and cost + 1 < visited_cost[(straight, direction)]:
            visited_cost[(straight, direction)] = cost + 1
            visited_parent[(straight, direction)] = [current]
            heapq.heappush(min_pq, (cost + 1, (straight, direction)))

        #Process for a right turn
        right_turn = turn_right(direction)
        if cost + 1000 == visited_cost[(pos, right_turn)]:
                visited_parent[(pos, right_turn)].append((current))
        if cost + 1000 < visited_cost[(pos, right_turn)]:
            visited_cost[(pos, right_turn)] = cost + 1000
            visited_parent[(pos, right_turn)] = [current]
            heapq.heappush(min_pq, (cost + 1000, (pos, right_turn)))

        #Process for a left turn
        left_turn = turn_left(direction)
        if cost + 1000 == visited_cost[(pos, left_turn)]:
                visited_parent[(pos, left_turn)].append((current))
        if cost + 1000 < visited_cost[(pos, left_turn)]:
            visited_cost[(pos, left_turn)] = cost + 1000
            visited_parent[(pos, left_turn)] = [current]
            heapq.heappush(min_pq, (cost + 1000, (pos, left_turn)))

    optimal_tiles = set()
    #Have to add finish to the set since find_optimal_tiles does not
    optimal_tiles.add(finish)
    #This goes backward through visited recursively and starts with finish's parents
    find_optimal_tiles(visited_parent, current, reindeer, optimal_tiles)
    return min_cost, len(optimal_tiles)
        
if __name__ == '__main__':
    DEBUG = True
    maze, MAXY, MAXX = load_data('input')
    tiles, reindeer, finish = mapify(maze)
    cheapest, num_optimal = shortest_path(reindeer, (0,1), finish, tiles)
    print(num_optimal)
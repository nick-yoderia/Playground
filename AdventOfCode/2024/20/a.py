from collections import defaultdict
import heapq
import math
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

def shortest_path(tiles, start, finish):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited_cost = defaultdict(lambda: math.inf)
    prev = {}
    min_pq = []
    min_cost = math.inf
    heapq.heappush(min_pq, (0, start))
    visited_cost[start] = 0

    while min_pq:
        cost, pos = heapq.heappop(min_pq)
        y, x = pos

        if pos == finish:
            min_cost = cost
            break

        for dy, dx in directions:
            next_y, next_x = (y + dy, x + dx)
            next_pos = (next_y, next_x)
            if 0 <= next_x < MAXX and 0 <= next_y < MAXY and cost + 1 < visited_cost[next_pos] and next_pos in tiles:
                visited_cost[next_pos] = cost + 1
                prev[next_pos] = pos
                heapq.heappush(min_pq, (cost + 1, next_pos))

    # Reconstruct path
    path = []
    if min_cost != math.inf:
        node = finish
        while node != start:
            path.append(node)
            node = prev[node]
        path.append(start)
        path.reverse()
    return min_cost, path

def find_cheats(pos, tiles, valid=None, depth=0):
    if valid is None:
        valid = set()
    if depth == 2:
        return valid
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in directions:
        new_pos = pos[0]+dy, pos[1]+dx
        if new_pos in tiles:
            valid.add((depth+1, new_pos))
        find_cheats(new_pos, tiles, valid, depth + 1)
    return valid

def cheat_saves(path, tiles, no_cheats, costs):
    saves = defaultdict(int)
    for i, pos in enumerate(path):
        for cheat in find_cheats(pos, tiles):
            save = i + cheat[0] + costs[cheat[1]]
            if save < no_cheats-1:
                saves[no_cheats-save] += 1
    return saves

if __name__ == '__main__':
    start_time = time.perf_counter()
    track, MAXY, MAXX = load_data('input')
    tiles, start, finish = mapify(track)
    no_cheats, path = shortest_path(tiles, start, finish)
    costs = {}
    for tile in tiles:
        score, _ = shortest_path(tiles, tile, finish)
        costs[tile] = score
    saves = cheat_saves(path, tiles, no_cheats, costs)
    total = 0
    for key in saves:
        if key >= 100:
            total += saves[key]
    print(total)
    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")
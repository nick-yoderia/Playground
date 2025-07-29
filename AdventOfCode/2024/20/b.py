from collections import defaultdict
import heapq
import math

def load_data(input):
    with open(input, 'r') as file:
        maze = file.read()
        maze = maze.splitlines()
        maze = [line.strip() for line in maze]
        maxy, maxx = len(maze), len(maze[0])
    return maze, maxy, maxx

def mapify(maze):
    tiles = set()
    walls = set()
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
            else:
                walls.add((y,x))
    return tiles, walls, start, finish

def shortest_path(tiles, start, finish, max_depth=math.inf):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited_cost = defaultdict(lambda: math.inf)
    prev = {}
    min_pq = []
    min_cost = math.inf
    heapq.heappush(min_pq, (0, start))
    visited_cost[start] = 0

    while min_pq:
        cost, pos = heapq.heappop(min_pq)
        if cost > max_depth:
            continue
        y, x = pos
        if pos == finish:
            min_cost = cost
            break
        for dy, dx in directions:
            next_y, next_x = (y + dy, x + dx)
            next_pos = (next_y, next_x)
            if next_pos in tiles and cost + 1 < visited_cost[next_pos]:
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

if __name__ == '__main__':
    track, MAXY, MAXX = load_data('input')
    tiles, walls, start, finish = mapify(track)
    max_cost, main_path = shortest_path(tiles, start, finish)
    saves = defaultdict(int)
    for i, node in enumerate(main_path):
        if i+100 >= len(main_path):
            break
        for j in range(i+100, len(main_path)):
            sub_node = main_path[j]
            non_cheat_cost = j - i
            sub_walls = set(walls)
            sub_walls.update([node, sub_node])
            cheat_cost, cheat_path = shortest_path(sub_walls, node, sub_node, 2)
            if len(cheat_path)-1 <= 2 and cheat_cost < non_cheat_cost:
                saves[non_cheat_cost-cheat_cost] += 1
    
    # for key in saves:
    #     print(f"There are {saves[key]} that save {key} picoseconds.")

    total = 0
    for key in saves:
        if key >= 100:
            total += saves[key]
    print(total)

from collections import defaultdict
import heapq
import math
import os

def load_data(input):
    with open(input, 'r') as file:
        data = file.readlines()
        coords = []
        for line in data:
            items = line.strip().split(',')
            if len(items) == 2:
                coords.append((int(items[0]), int(items[1])))
        return coords
    
def simulate(num, coords):
    corrupted = set()
    for i in range(num):
        corrupted.add(coords[i])
    return corrupted

def shortest_path(corrupted):
    finish = (MAXX, MAXY)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited_cost = defaultdict(lambda: math.inf)
    min_pq = []
    min_cost = 0
    heapq.heappush(min_pq, (0, (0, 0)))

    while min_pq:
        cost, pos = heapq.heappop(min_pq)
        x, y = pos

        #Found shortest path
        if pos == finish:
            min_cost = cost
            break
        
        for dx, dy in directions:
            next_x, next_y = (x + dx, y + dy)
            if 0 <= next_x <= MAXX and 0 <= next_y <= MAXY and cost + 1 < visited_cost[(next_x, next_y)] and (next_x, next_y) not in corrupted:
                visited_cost[(next_x, next_y)] = cost + 1
                heapq.heappush(min_pq, (cost + 1, (next_x, next_y)))

    return min_cost
    
def draw_map(corrupted):
    lines = []
    for y in range(MAXY+1):
        line = []
        for x in range(MAXX+1):
            if (x,y) in corrupted:
                line.append('#')
            else:
                line.append('.')
        lines.append("".join(line))
    # os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(lines))


if __name__ == "__main__":
    MAXX = MAXY = 70
    coords = load_data('input')
    corrupted = simulate(1024, coords)    
    print(shortest_path(corrupted))
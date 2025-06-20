import re
import os
from functools import reduce
import msvcrt

MAXX, MAXY = 101, 103

def load_data(input):
    robots = []
    with open(input, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for line in lines:
            robots.append(list(map(int, re.findall(r'-?\d+', line))))
    return robots

def simulate_robots(robots: list, dist=1):
    new_robots = []
    for robot in robots:
        x, y = robot[0], robot[1]
        dx, dy = robot[2], robot[3]
        x = (x + dx * dist) % MAXX
        y = (y + dy * dist) % MAXY
        new_robots.append([x, y, dx, dy])
    return new_robots

def get_quadrants(end_positions: dict):
    quad1 = quad2 = quad3 = quad4 = 0
    for end_pos in end_positions.keys():
        x, y = end_pos
        if y < MAXY // 2:
            if x < MAXX // 2:
                quad1 += end_positions[end_pos]
            elif x > MAXX // 2 - 1 + MAXX % 2:
                quad2 += end_positions[end_pos]
        elif y > MAXY // 2 - 1 + MAXY % 2:
            if x < MAXX // 2:
                quad3 += end_positions[end_pos]
            elif x > MAXX // 2 - 1 + MAXX % 2:
                quad4 += end_positions[end_pos]
    return (quad1, quad2, quad3, quad4)

def draw_map(robots_dict: dict, seconds):
    rows = []
    for i in range(MAXY):
        row = []
        for j in range(MAXX):
            if (j, i) in robots_dict:
                row.append(str(robots_dict[(j,i)]))
            else:
                row.append('.')
        rows.append(''.join(row))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(rows))
    print(f"\n{seconds} Seconds\n")

def find_convergence(a, b):
    num = 1
    while(True):
        if num % a == 0 and num % b == 0:
            return num
        else:
            num += 1

if __name__ == '__main__':
    robots = load_data('input')
    end_positions = {}
    # Change dist and cur_time accordingly
    dist = 101*103 # This is how many seconds you want to iterate by
    cur_time = 7687 # This is just your starting time
    robots = simulate_robots(robots, cur_time)
    while True:
        robots_dict = {}
        for robot in robots:
            key = (robot[0], robot[1])
            robots_dict[key] = robots_dict.get(key, 0) + 1
        draw_map(robots_dict, cur_time)
        key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'M':
                robots = simulate_robots(robots, dist)
                cur_time += dist
            elif key == b'K':
                robots = simulate_robots(robots, -dist)
                cur_time -= dist
        elif key.lower() == b'q':
            break
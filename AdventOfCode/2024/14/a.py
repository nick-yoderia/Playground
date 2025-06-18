import re
import os
import time
from functools import reduce
import operator

MAXX, MAXY = 101, 103

def load_data(input):
    robots = []
    with open(input, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for line in lines:
            robots.append(list(map(int, re.findall(r'-?\d+', line))))
    return robots

def simulate_robot(robot: list, seconds, visualize=False):
    x, y = robot[0], robot[1]
    dx, dy = robot[2], robot[3]
    while(seconds > 0):
        x = (x + dx) % MAXX
        y = (y + dy) % MAXY
        seconds -= 1
        if visualize: draw_robot_path((x,y))
    return (x, y)

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

def draw_robot_path(coords):
    rows = []
    for i in range(MAXY):
        row = []
        for j in range(MAXX):
            if j == coords[0] and i == coords[1]:
                row.append('#')
            else:
                row.append('.')
        rows.append(' '.join(row))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(rows))
    time.sleep(0.1)
    
if __name__ == '__main__':
    robots = load_data('input')
    end_positions = {}
    seconds = 100
    for robot in robots:
        end_pos = simulate_robot(robot, seconds)
        end_positions[end_pos] = end_positions.get(end_pos, 0) + 1
    quads = get_quadrants(end_positions)
    print(f"Quadrants = {quads}")
    print(f"Safety factor of {reduce(operator.mul, quads, 1)}")
import re
import math
from functools import lru_cache
from collections import deque

def load_data(input):
    with open(input, "r") as file:
        # [[A -> (dx, dy), B -> (dx, dy), (x, y)]]
        machines = []
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for i in range(0, len(lines), 3):
            a_nums = list(map(int, re.findall(r'-?\d+', lines[i])))
            b_nums = list(map(int, re.findall(r'-?\d+', lines[i+1])))
            dest_nums = re.findall(r'-?\d+', lines[i+2])
            a_dx, a_dy = a_nums[0], a_nums[1]
            b_dx, b_dy = b_nums[0], b_nums[1]
            x, y = int(str(10000000000000) + dest_nums[0]), int(str(10000000000000) + dest_nums[1])
            machines.append([(a_dx, a_dy), (b_dx, b_dy), (x, y)])
    return machines

def find_cheapest_path(machine):
    # unpack the machine
    a = tuple(machine[0])
    b = tuple(machine[1])
    dest = tuple(machine[2])
    return cheapest_helper(0, 0, a, b, dest)

def cheapest_helper(x, y, a, b, dest):
    if x > dest[0] or y > dest[1]:
        return float('inf')
    if x == dest[0] and y == dest[1]:
        return 0
    a_button = 3 + cheapest_helper(x + a[0], y + a[1], a, b, dest)
    b_button = 1 + cheapest_helper(x + b[0], y + b[1], a, b, dest)
    return min(a_button, b_button)

if __name__ == '__main__':
    machines = load_data('input')
    total_tokens = 0
    for machine in machines:
        cheapest = find_cheapest_path(machine)
        if not math.isinf(cheapest): total_tokens += cheapest
    print(total_tokens)
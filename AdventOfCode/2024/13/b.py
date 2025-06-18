import re
import math
from functools import lru_cache

def load_data(input):
    with open(input, "r") as file:
        # [[A -> (dx, dy), B -> (dx, dy), (x, y)]]
        machines = []
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for i in range(0, len(lines), 3):
            a_nums = list(map(int, re.findall(r'-?\d+', lines[i])))
            b_nums = list(map(int, re.findall(r'-?\d+', lines[i+1])))
            dest_nums = list(map(int, re.findall(r'-?\d+', lines[i+2])))
            a_dx, a_dy = a_nums[0], a_nums[1]
            b_dx, b_dy = b_nums[0], b_nums[1]
            x, y = 10000000000000 + dest_nums[0], 10000000000000 + dest_nums[1]
            machines.append([(a_dx, a_dy), (b_dx, b_dy), (x, y)])
    return machines


def find_cheapest_path(machine):
    ax, ay = machine[0]
    bx, by = machine[1]
    dest_x, dest_y = machine[2]
    #a_count = (dest_y*bx - dest_x*by)/(ay*bx - ax*by)
    numerator = dest_y*bx - dest_x*by
    denominator = ay*bx - ax*by
    if denominator == 0:
        if dest_x % ax == 0 and dest_y % ay == 0:
            a_count = dest_x/ax
            b_count = dest_x/bx
            tokens = min(3*a_count, b_count)
            return tokens if tokens % 1 == 0 else 0
        else:
            return 0
    if numerator % denominator != 0:
        return 0
    a_count = numerator / denominator
    b_count = (dest_x - a_count * ax) / bx
    if b_count % 1 != 0:
        return 0
    if a_count < 0 or b_count < 0:
        return 0
    return int(b_count + 3 * a_count)

if __name__ == '__main__':
    machines = load_data('input')
    total_tokens = 0
    for machine in machines:
        cheapest = find_cheapest_path(machine)
        total_tokens += cheapest
    print(total_tokens)
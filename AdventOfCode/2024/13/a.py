import re
from functools import lru_cache

def load_data(input):
    with open(input, "r") as file:
        # [[A -> (dx, dy), B -> (dx, dy), (x, y)]]
        machines = []
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for i in range(0, len(lines), 3):
            a_dx, a_dy = re.findall(r'\d+', lines[i])
            b_dx, b_dy = re.findall(r'\d+', lines[i+1])
            x, y = re.findall(r'\d+', lines[i+2])
            machines.append([(int(a_dx), int(a_dy)), (int(b_dx), int(b_dy)), (int(x), int(y))])
    return machines

def find_cheapest_path(machine):
    # unpack the machine
    a = machine[0]
    b = machine[1]
    dest = machine[2]
    return cheapest_helper(0, 0, a, b, dest)

@lru_cache(maxsize=None)
def cheapest_helper(x, y, a, b, dest):
    if x > dest[0] or y > dest[1]:
        return 9999
    if x == dest[0] or y == dest[1]:
        return 0
    left = 1 + cheapest_helper(x + a[0], y + a[1], a, b, dest)
    right = 3 + cheapest_helper(x + b[0], y + b[1], a, b, dest)
    return left if left < right else right

if __name__ == '__main__':
    machines = load_data('input')
    print(machines)
    for machine in machines:
        cheapest = find_cheapest_path(machine)
        print(cheapest)



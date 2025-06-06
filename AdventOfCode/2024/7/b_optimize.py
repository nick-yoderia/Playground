import re
import time
from itertools import product

# returns a list of numbers symbolizing an equation
def load(input):
    with open(input, "r") as file:
        lines = [line.strip() for line in file]
        return [list(map(int, re.findall(r"\d+", line))) for line in lines]

def valid_equation(equation):
    result = equation[0]
    values = equation[1:]
    n = len(values)

    for ops in product((0, 1, 2), repeat=n-1):
        sum = values[0]
        for i, op in enumerate(ops, 1):
            val = values[i]
            if op == 0:
                sum += val
            elif op == 1:
                sum *= val
            else:
                sum = sum * 10**(len(str(val))) + val
            if sum > result:
                break
        if sum == result:
            return result
    return 0

if __name__ == "__main__":
    start_time = time.perf_counter()
    equations = load("./input")
    sum = 0

    for equation in equations:
        result = valid_equation(equation)
        sum += result

    end_time = time.perf_counter()
    print(sum)
    print("Runtime: {:f} seconds".format(end_time - start_time))
import re
import time

# returns a list of numbers symbolizing an equation
def load(input):
    with open(input, "r") as file:
        lines = [line.strip() for line in file]
        return [list(map(int, re.findall(r"\d+", line))) for line in lines]

def check_valid(i, current, values, length, result):
        # base conditional
        if i == length:
            return current == result
        
        val = values[i]

        if current * val <= result and check_valid(i + 1, current * val, values, length, result):
            return True
        
        union = current * 10**(len(str(val))) + val
        if union <= result and check_valid(i + 1, union, values, length, result):
            return True
        
        if current + val <= result and check_valid(i + 1, current + val, values, length, result):
            return True
        return False

def valid_equation(equation):
    result = equation[0]
    values = equation[1:]
    length = len(values)

    if check_valid(1, values[0], values, length, result):
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
    print(f"Runtime: {end_time - start_time:f} seconds")
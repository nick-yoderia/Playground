import re
import time

# returns a list of numbers symbolizing a 
def load(input):
    with open(input, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return [re.findall(r"\d+", line) for line in lines]

def to_base3(num, length):
    digits = []
    for _ in range(length):
        digits.append(str(num % 3))
        num //= 3
    return ''.join(reversed(digits))

def valid_equation(equation):
    result = int(equation[0])
    values = equation[1:]
    length = len(values)
    for i in range(0, 3 ** (length-1)):
        sum = int(values[0])
        base3_str = to_base3(i, length - 1)
        for j, char in enumerate(base3_str, 1):
            if char == '0':
                sum += int(values[j])
            elif char == '1':
                sum *= int(values[j])
            else:
                sum = int(str(sum) + values[j])
            if sum > result: break
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
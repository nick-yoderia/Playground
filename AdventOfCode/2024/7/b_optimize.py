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
    length = len(equation[1:])
    operators = []
    for i in range(0, 3 ** (length-1)):
        operators.append(to_base3(i, length - 1))
    while(len(operators) > 1):
        operator = operators[len(operators) // 2]
        midpoint = valid_equation_helper(equation, operator)
        if midpoint < result:
            operators = operators[:len(operators) // 2]
        elif midpoint > result:
            operators = operators[len(operators) // 2:]
        else:
            return result
    final_test = valid_equation_helper(equation, operators[0])
    if final_test == result:
        print(equation)
        return result
    return 0

def valid_equation_helper(equation, operator):
    values = equation[1:]
    sum = int(equation[1])
    for i, char in enumerate(operator, 1):
        if char == '0':
            sum += int(values[i])
        elif char == '1':
            sum *= int(values[i])
        else:
            sum = int(str(sum) + values[i])
    return sum


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
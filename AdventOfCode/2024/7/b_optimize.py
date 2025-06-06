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
    operators = []
    for i in range(0, 3 ** (length)):
        operators.append(to_base3(i, length))

    operator_parts = {}
    for operator in operators:
        sum = valid_equation_helper(values, operator, operator_parts)
        if sum == result:
            return result
    return 0

def valid_equation_helper(values, operator, operator_parts):
    sum = int(values[0])
    for i in range(1, len(operator)):
        if operator[:i] in operator_parts:
            sum = operator_parts[operator[:i]]
        else:
            match operator[i-1]:
                case '0':
                    sum += int(values[i])
                case '1':
                    sum *= int(values[i])
                case _:
                    sum = int(str(sum) + values[i])
            operator_parts[operator[:i]] = sum
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
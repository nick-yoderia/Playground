import re

# returns a list of numbers symbolizing a 
def load(input):
    with open(input, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return [re.findall(r"\d+", line) for line in lines]

def valid_equation(equation):
    result = equation[0]
    values = equation[1:]
    length = len(values)
    for i in range(0, 2 ** (length-1)):
        sum = values[0]
        binary_str = f"{i:0{length - 1}b}"
        for j, char in enumerate(binary_str, 1):
            if char == '0':
                sum += values[j]
            else:
                sum *= values[j]
        if sum == result: return result
    return 0

if __name__ == "__main__":

    equations = load("./input")

    sum = 0

    for i , equation in enumerate(equations, 1):
        equation = [int(num) for num in equation]
        result = valid_equation(equation)
        sum += result

    print(sum)
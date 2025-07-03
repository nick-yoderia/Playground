import time

def load_data(input):
    with open(input, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            if line.strip():
                data.append(line.split(':')[1].strip())
    a, b, c, program = data
    program = program.split(',')
    return int(a), int(b), int(c), list(map(int, program))

# opcode 0
def adv(operand, a):
    return a // 1>>operand

# opcode 1
def bxl(operand, b):
    return b ^ operand

# opcode 2
def bst(operand):
    return operand % 8

# opcode 3
def jnz(operand, a):
    if a != 0:
        return operand

# opcode 4
def bxc(b, c):
    return b ^ c

# opcode 5
def out(operand, output: list):
    output.append(operand % 8)

# opcode 6
def bdv(operand, a):
    return a // 1>>operand

# opcode 7
def cdv(operand, a):
    return a // 1>>operand

def run_program(a: str, b, c, program):
    # a comes in as a string representing a base 8 number
    a = int(a, 8)
    output = []
    i = 0
    while i < len(program):
        instruction = program[i]
        if i+1 < len(program):
            operand = program[i+1]
            match operand:
                case 4:
                    operand_value = a
                case 5:
                    operand_value = b
                case 6:
                    operand_value = c
                case _:
                    operand_value = operand

            match instruction:
                case 0:
                    a = adv(operand_value, a)
                    i += 2
                case 1:
                    b = bxl(operand, b)
                    i += 2
                case 2:
                    b = bst(operand_value)
                    i += 2
                case 3:
                    new_i = jnz(operand, a)
                    if new_i is not None:
                        i = new_i
                    else:
                        i += 2
                case 4:
                    b = bxc(b, c)
                    i += 2
                case 5:
                    out(operand_value, output)
                    i += 2
                case 6:
                    b = bdv(operand_value, a)
                    i += 2
                case 7:
                    c = cdv(operand_value, a)
                    i += 2
        else:
            i += 1
    return output

def recursive_test(a: str, b, c, program, solutions: list):
    # a is a string representing an octal
    output = run_program(a, b, c, program)
    if output == program:
        solutions.append(int(a, 8))
        return
    elif len(a) <= len(program) and output == program[-len(output):]:
        for i in range(8):
            recursive_test(a+str(i), b, c, program, solutions)

if __name__ == '__main__':
    _, b, c, program = load_data('input')
    solutions = []
    starting_octals = []

    # start the clock
    start_time = time.perf_counter()
    # find most significant octal
    for i in range(8):
        output = run_program(str(i), b, c, program)
        if output == program[-len(output):]:
            starting_octals.append(str(i))

    # dfs on all potential answers
    for a in starting_octals:
        recursive_test(a, b, c, program, solutions)

    # end the clock
    end_time = time.perf_counter()

    # print results
    print(f"{end_time-start_time:f} seconds")
    print(min(solutions))

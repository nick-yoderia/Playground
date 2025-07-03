import sys
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

def run_program(a, b, c, program, optimize):
    output = []
    a_start = a
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
                    index = len(output) - 1
                    if optimize and (index > len(program) or output[index] != program[index]):
                        return a_start + 1, True, True
                    i += 2
                case 6:
                    b = bdv(operand_value, a)
                    i += 2
                case 7:
                    c = cdv(operand_value, a)
                    i += 2
        else:
            i += 1
    if output == program:
        return a_start, False, True
    elif len(output) < len(program):
        # print(f"{"".join(map(str, output))} != {"".join(map(str, program))}")
        return a_start*10, True, False
    else:
        return a_start+1, True, True

if __name__ == '__main__':
    start_time = time.perf_counter()
    a, b, c, program = load_data('input')
    a = 1
    flag = True
    optimize = False
    while flag:
        a, flag, optimize = run_program(a,b,c, program, optimize)
    print(a)
    end_time = time.perf_counter()
    print(f"{end_time - start_time:f} seconds")
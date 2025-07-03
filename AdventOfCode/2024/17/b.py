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

def run_program(a, b, c, program):
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
        return a_start, False
    elif len(output) < len(program):
        return 8**(len(program) - len(output)), True
    elif len(output) == len(program):
        matching = num_matching(output, program)
        diff = len(program) - matching
        return a_start+8**(diff-1), True

def num_matching(arr1, arr2):
    matching = 0
    for i in range(min(len(arr1), len(arr2))):
        if arr1[i] == arr2[i]:
            matching += 1
    return matching

if __name__ == '__main__':
    start_time = time.perf_counter()
    a, b, c, program = load_data('input')
    a = 1
    flag = True
    while flag:
        a, flag = run_program(a,b,c, program)
    print(a)
    end_time = time.perf_counter()
    print(f"{end_time - start_time:f} seconds")
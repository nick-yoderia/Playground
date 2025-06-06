from math import log
import time

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.rstrip())
    return data

def calc(target: int, operands: list) -> int:
    partials = [operands[0]]
    for i in range(1, len(operands)):
        operand = operands[i]
        newpartials = []
        for p in partials:
            t = p + operand
            if t <= target:
                newpartials.append(t)

            t = p * operand
            if t <= target:
                newpartials.append(t)

            t = p*10**(len(str(operand))) + operand
            if t <= target:
                newpartials.append(t)
        if len(newpartials) == 0: return 0 #prevents lines 14 & 15 repeating for excessive iterations
        partials = newpartials
    if target in partials:
        return target
    return 0

if __name__ == "__main__":

    start_time = time.perf_counter()

    data = load_data("./input")

    total = 0
    for line in data:
        target, operands = line.split(": ")
        operands = operands.split()
        total += calc(int(target), list(map(int, operands)))

    end_time = time.perf_counter()
    print(total)
    print(f"Runtime: {end_time - start_time:f} seconds")
import sys
from functools import lru_cache

def load_data(input):
    with open(input, 'r') as file:
        text = file.read().strip()
        text = text.split()
    return text

@lru_cache(maxsize=None)
def blink(stone, iterations):
    if iterations == 0:
        return 0
    if stone == '0':
        return blink('1', iterations-1)
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        left = stone[:mid]
        right = stone[mid:].lstrip('0') or '0'
        return 1 + blink(left, iterations - 1) + blink(right, iterations - 1)
    else:
        return blink(str(int(stone) * 2024), iterations - 1)

if __name__ == '__main__':
    data = load_data('input')
    length = []
    for stone in data:
        # Always one less because starting stone not included
        length.append(blink(stone, int(sys.argv[1])) + 1)
    print(sum(length))
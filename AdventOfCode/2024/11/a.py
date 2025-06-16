import sys

def load_data(input):
    with open(input, 'r') as file:
        text = file.read().strip()
        text = text.split()
    return text

def blink_once(text):
    new_text = []
    for stone in text:
        if stone == '0':
            new_text.append('1')
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            new_text.append(stone[:mid])
            new_text.append(stone[mid:].lstrip('0') or '0')
        else:
            new_text.append(str(int(stone) * 2024))
    return new_text

def blink(num_times, text):
    for _ in range(num_times):
        text = blink_once(text)
    return text

if __name__ == '__main__':
    data = load_data('input')
    new_text = blink(int(sys.argv[1]), data)
    print(len(new_text))
import re

def load_data(input):
    with open(input, 'r') as file:
        text = file.read().strip().replace('\n', '')
    return text

def uncompress(data: str) -> str:
    result = ''
    files = True #starts with files
    file_count = 0
    for i in range(len(data)):
        if files:
            for j in range(int(data[i])):
                result += str(file_count)
            file_count += 1
        else:
            for j in range(int(data[i])):
                result += '.'
        files = not files
    return result


def compress(data: str):
    reverse_data = data[::-1]
    block_pattern = r"\.+"
    digit_pattern = r"(\d)\1*"
    for digit_match in re.finditer(digit_pattern, reverse_data):
        for block_match in re.finditer(block_pattern, data):
            if block_match.start() > len(data) - digit_match.end():
                break
            block_length = block_match.end() - block_match.start()
            digit_length = digit_match.end() - digit_match.start()
            if block_length >= digit_length:
                difference = block_length - digit_length
                data = data[:block_match.start()] + digit_match.group() + '.' * difference + data[block_match.end():]
                data = data[:len(data) - digit_match.end()] + '.' * digit_length + data[len(data) - digit_match.start():]
                reverse_data = data[::-1]
                break
    return data

def stringify(data):
    string = ''
    for char_list in data:
        for char in char_list:
            string += char
    return string

def checksum(data: str):
    sum = 0
    for i in range(len(data)):
        if data[i] != '.':
            sum += i * int(data[i])
    return sum

if __name__ == '__main__':
    input = 'input'
    data = load_data(input)
    result = uncompress(data)
    result = compress(result)
    print(checksum(result))
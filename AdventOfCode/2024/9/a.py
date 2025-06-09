def load_data(input):
    with open(input, 'r') as file:
        text = file.read().strip().replace('\n', '')
    return text

def uncompress(data: str) -> list:
    result = []
    files = True #starts with files
    file_count = 0
    for i in range(len(data)):
        if files:
            for j in range(int(data[i])):
                result.append(str(file_count))
            file_count += 1
        else:
            for j in range(int(data[i])):
                result.append('.')
        files = not files
    return result

def compress(data: list):
    i = 0
    j = len(data) - 1
    while i < j:
        if data[i] != '.':
            i += 1
            continue
        if data[j] == '.':
            j -= 1
        else:
            data[i], data[j] = data[j], '.'
            i += 1
            j -= 1
    return data

def checksum(data: list):
    sum = 0
    for i in range(len(data)):
        if data[i] != '.':
            sum += i * int(data[i])
        else:
            break
    return sum

if __name__ == '__main__':
    input = 'input'
    data = load_data(input)
    result = uncompress(data)
    result = compress(result)
    print(''.join(result))
    print(checksum(result))
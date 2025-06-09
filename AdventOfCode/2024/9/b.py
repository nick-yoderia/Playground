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

def chunkify(data: list) -> list:
    result = []
    chunk = []
    current = data[0]
    for file in data:
        if file == current:
            chunk.append(file)
        else:
            current = file
            result.append(chunk)
            chunk = [current]
    result.append(chunk)
    return result

def compress(data: list):
    end_point = len(data) - 1
    data = data[:]
    for i in range(end_point, 0, -1):
        if data[i][0] != '.':
            for j in range(0, i):
                if data[j][0] == '.' and len(data[i]) <= len(data[j]):
                    length_file = len(data[j])
                    length_block = len(data[i])
                    data[j] = data[i]
                    if length_file > len(data[j]):
                        data.insert(j+1, ['.' for _ in range(length_file - len(data[i]))])
                        i += 1
                    data[i] = ['.' for _ in range(length_block)]
                    print(stringify(data))
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
    result = chunkify(result)
    result = compress(result)
    result = stringify(result)
    print(checksum(result))
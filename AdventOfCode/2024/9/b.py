import re

def load_data(input):
    with open(input, 'r') as file:
        text = file.read().strip().replace('\n', '')
    return text

def uncompress(data: str) -> str:
    result = []
    files = True #starts with files
    file_count = 0
    for i in range(len(data)):
        if files:
            result.append([file_count, int(data[i])])
            file_count += 1
        else:
            result.append([None, int(data[i])])
        files = not files
    return result

def compress(data: list):
    for i in range(len(data) - 1, -1, -1):
        if data[i][0] == None:
            continue
        for j in range(0, i):
            if data[j][0] == None and data[j][1] >= data[i][1]:
                if data[j][1] == data[i][1]:
                    data[j], data[i] = data[i], data[j]
                    break
                else:
                    diff = data[j][1] - data[i][1]
                    data[j], data[i] = data[i], data[j]
                    data[i][1] -= diff
                    if data[j+1][0] == None:
                        data[j+1][1] += diff
                    else:
                        data.insert(j+1, [None, diff])
                        i += 1
                    break
    return [x for x in data if x[1] > 0]

def stringify(data):
    long_data = []
    for file in data:
        for i in range(file[1]):
            if file[0] == None:
                long_data.append(None)
            else:
                long_data.append(str(file[0]))
    return long_data

def checksum(data: str):
    sum = 0
    for i in range(len(data)):
        if data[i] != None:
            sum += i * int(data[i])
    return sum

if __name__ == '__main__':
    input = 'input'
    data = load_data(input)
    result = uncompress(data)
    result = compress(result)
    result = stringify(result)
    print(checksum(result))
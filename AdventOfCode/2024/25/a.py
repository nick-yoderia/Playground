def load_data(input):
    with open(input, 'r') as file:
        keys_and_locks = file.read().split('\n\n')
        keys_and_locks = [key_or_lock.split('\n') for key_or_lock in keys_and_locks]
    return keys_and_locks

def analyze(raw):
    keys = set()
    locks = set()
    for item in raw:
        if item[0][0] == '.':
            item = item[:-1]
            isKey = True
        else:
            item = item[1:]
            isKey = False
        analyzed = [0] * len(item[0])
        for row in item:
            for i, column in enumerate(row):
                if column == '#':
                    analyzed[i] += 1
        if isKey:
            keys.add(tuple(analyzed))
        else:
            locks.add(tuple(analyzed))
    return keys, locks


if __name__ == '__main__':
    keys_and_locks = load_data('input')

    keys, locks = analyze(keys_and_locks)

    pairs = 0
    for key in keys:
        for lock in locks:
            match = True
            for i in range(len(key)):
                if key[i] + lock[i] > 5:
                    match = False
                    continue
            if match: pairs += 1

    print(pairs)
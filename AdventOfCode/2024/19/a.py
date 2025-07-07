def load_data(input):
    with open(input, 'r') as file:
        data = file.read().split('\n\n')
        towels = set(item.strip() for item in data[0].split(','))
        patterns = [item.strip() for item in data[1].split('\n')]
        return towels, patterns

def is_valid(towels, pattern):
    if not pattern:
        return True
    for towel in towels:
        if pattern[:len(towel)] == towel:
            if is_valid(towels, pattern[len(towel):]):
                return True

def get_valid_count(towels: set, patterns: list):
    count = 0
    for pattern in patterns:
        if is_valid(towels, pattern):
            count += 1
    return count

if __name__ == '__main__':
    towels, patterns = load_data('input')
    count = get_valid_count(towels, patterns)
    print(count)
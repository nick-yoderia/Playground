from functools import lru_cache

def load_data(input):
    with open(input, 'r') as file:
        data = file.read().split('\n\n')
        towels = [item.strip() for item in data[0].split(',')]
        patterns = [item.strip() for item in data[1].split('\n')]
        return towels, patterns

def is_valid(pattern, towels, memo={}):
    if pattern in memo:
        return memo[pattern]
    count = 0
    if not pattern:
        return 1
    for towel in towels:
        if pattern.startswith(towel):
            count += is_valid(pattern[len(towel):], towels, memo)
    memo[pattern] = count
    return count

def get_valid_count(patterns: list, towels: list):
    count = 0
    memo = {}
    for pattern in patterns:
        count += is_valid(pattern, towels, memo)
    return count

if __name__ == '__main__':
    towels, patterns = load_data('input')
    count = get_valid_count(patterns, towels)
    print(count)
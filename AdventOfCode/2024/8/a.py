def load_data(input_file):
    antenas = {}
    with open(input_file, 'r') as file:
        lines = file.readlines()
        maxy = len(lines)
        maxx = len(lines[0].strip())
        for y, line in enumerate(lines):
            line = line.strip()
            for x, char in enumerate(line):
                if char != '.':
                    antenas.setdefault(char, []).append((x, y))
    return maxx, maxy, antenas

def prune_result(results, maxx, maxy):
    pruned = set()
    for result in results:
        x, y = result
        if 0 <= x < maxx and 0 <= y < maxy:
            pruned.add((x, y))
    return pruned

def find_antinodes(antenas):
    results = set()
    for antena in antenas:
        positions = set(antenas[antena])
        for ord_x, ord_y in positions:
            for alt_x, alt_y in positions:
                if (ord_x, ord_y) != (alt_x, alt_y):
                    dx = ord_x - alt_x
                    dy = ord_y - alt_y
                    results.add((ord_x+dx, ord_y+dy))
                    results.add((alt_x-dx, alt_y-dy))
    return results

if __name__ == "__main__":
    
    maxx, maxy, antenas = load_data("input")
    results = find_antinodes(antenas)
    results = prune_result(results, maxx, maxy)
    print(len(results))
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

def find_antinodes(antenas):
    results = set()
    for antena in antenas:
        positions = set(antenas[antena])
        for org_x, org_y in positions:
            for alt_x, alt_y in positions:
                if (org_x, org_y) != (alt_x, alt_y):
                    dx = org_x - alt_x
                    dy = org_y - alt_y
                    # Add antinodes to original and alternate positions
                    results.add((org_x, org_y))
                    results.add((alt_x, alt_y))
                    # Draw antinodes in org -> alt direction
                    start_x = org_x + dx
                    start_y = org_y + dy
                    while 0 <= start_x <  maxx and 0 <= start_y < maxy:
                        results.add((start_x, start_y))
                        start_x += dx
                        start_y += dy
                    # Draw antinodes in alt -> org direction
                    start_x = alt_x - dx
                    start_y = alt_y - dy
                    while 0 <= start_x <  maxx and 0 <= start_y < maxy:
                        results.add((start_x, start_y))
                        start_x -= dx
                        start_y -= dy
    return results

if __name__ == "__main__":
    
    maxx, maxy, antenas = load_data("input")
    results = find_antinodes(antenas)
    print(len(results))
import itertools

class Pad:
    def __init__(self, layout):
        self.layout = layout
        self.coords_dict = self.get_coord_dict()

    def shortest_path(self, start, end):
        y1, x1 = start
        y2, x2 = end
        dy = y2 - y1
        dx = x2 - x1
        move = ''
        # Move vertically
        if dy < 0:
            move += '^' * abs(dy)
        elif dy > 0:
            move += 'v' * abs(dy)
        # Move horizontally
        if dx < 0:
            move += '<' * abs(dx)
        elif dx > 0:
            move += '>' * abs(dx)

        moves = [''.join(move) for move in itertools.permutations(move)]
        return moves
    
    def path_to_code(self, codes: list):
        cur_pos = self.coords_dict['A']
        paths = []
        for code in codes:
            for char in code:
                moves = self.shortest_path(cur_pos, self.coords_dict[char])
                if not paths:
                    paths = moves
                else:
                    new_paths = []
                    for path in paths:
                        for perm in moves:
                            new_path = path + perm
                            new_paths.append(new_path)
                    paths = new_paths
                for path in paths:
                    path += 'A'
                    cur_pos = self.coords_dict[char]
        # Find the minimum length among all paths
        min_length = min(len(path) for path in paths)
        # Return only those paths that have the minimum length
        return [path for path in paths if len(path) == min_length]

    def get_coord_dict(self):
        coords_dict = {}
        for y in range(len(self.layout)):
            for x in range(len(self.layout[0])):
                coords_dict[self.layout[y][x]] = (y,x)
        return coords_dict
    
if __name__ == '__main__':
    code = '0123'
    numpad_array = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            [None, '0', 'A']
        ]
    keypad_array = [
            [None,'^','A'],
            ['<','v','>']
        ]
    numpad = Pad(numpad_array)
    keypad = Pad(keypad_array)

    solutions = {}
    
    with open('input', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            path = numpad.path_to_code(line)
            for i in range(2):
                path = keypad.path_to_code(path)
            solutions[line] = path
    
    for entry in solutions:
        print(f"{entry}: {solutions[entry]}")

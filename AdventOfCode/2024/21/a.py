class Pad:
    def __init__(self, layout):
        self.layout = layout
        self.coords_dict = self.get_coord_dict()

    def shortest_path(self, start, end):
        y1, x1 = start
        y2, x2 = end
        dy = y2 - y1
        dx = x2 - x1
        # Choose move order with left first, then down, up, right
        path = []
        if dx < 0:
            path.append('<' * (-dx))
        if dy > 0:
            path.append('v' * dy)
        if dy < 0:
            path.append('^' * (-dy))
        if dx > 0:
            path.append('>' * dx)
        return "".join(path) + "A"
    
    def path_to_code(self, codes: list):
        cur_pos = self.coords_dict['A']
        path = []
        for code in codes:
            for char in code:
                path.append(self.shortest_path(cur_pos, self.coords_dict[char]))
                cur_pos = self.coords_dict[char]
        return ''.join(path)

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
        print(f"{entry}: {solutions[entry]} {len(solutions[entry])}")
        # print(f"{entry}: {len(solutions[entry])}")

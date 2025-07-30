class Pad:
    def __init__(self, layout):
        self.layout = layout
        self.coords_dict = self.get_coord_dict()

    def shortest_path(self, start, end):
        y1, x1 = start
        y2, x2 = end
        dy = y2 - y1
        dx = x2 - x1
        output = ''
        y_char = 'v' if dy > 0 else '^'
        x_char = '>' if dx > 0 else '<'
        if (y2, x1) not in self.coords_dict.values():
            output += x_char*abs(dx) + y_char*abs(dy)
        elif (y1, x2) not in self.coords_dict.values():
            output += y_char*abs(dy) + x_char*abs(dx)
        elif dx < 0:
            output += x_char*abs(dx) + y_char*abs(dy)
        else:
            output += y_char*abs(dy) + x_char*abs(dx)
        return output

    def path_to_code(self, codes: str):
        cur_pos = self.coords_dict['A']
        path = []
        for char in codes:
            path.append(self.shortest_path(cur_pos, self.coords_dict[char]))
            path.append('A')
            cur_pos = self.coords_dict[char]
        return ''.join(path)

    def get_coord_dict(self):
        coords_dict = {}
        for y in range(len(self.layout)):
            for x in range(len(self.layout[0])):
                if self.layout[y][x] is not None:
                    coords_dict[self.layout[y][x]] = (y,x)
        return coords_dict

if __name__ == '__main__':
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
    
    answer = 0
    for entry in solutions:
        print(f"{entry}: {solutions[entry]} {len(solutions[entry])}")
        # print(f"{entry}: {len(solutions[entry])}")
        answer += len(solutions[entry])*int(entry[:-1])
    print(f"Answer: {answer}")

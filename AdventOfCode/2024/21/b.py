from functools import lru_cache

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
        return output + 'A'

    def get_coord_dict(self):
        coords_dict = {}
        for y in range(len(self.layout)):
            for x in range(len(self.layout[0])):
                if self.layout[y][x] is not None:
                    coords_dict[self.layout[y][x]] = (y,x)
        return coords_dict
    
    def __init_subclass__(cls):
        super().__init_subclass__()
        if not hasattr(cls, 'path_to_code'):
            raise TypeError(f"{cls.__name__} must define 'path_to_code'")

class Keypad(Pad):
    def __init__(self):
        layout = [
            [None, '^', 'A'],
            ['<', 'v', '>']
        ]   
        super().__init__(layout)
    
    @lru_cache(maxsize=None)
    def path_to_code(self, codes: str, depth=1):
        cur_pos = self.coords_dict['A']
        path = 0
        if depth < 1:
            return len(codes)
        else:
            for char in codes:
                path += self.path_to_code(self.shortest_path(cur_pos, self.coords_dict[char]), depth - 1)
                cur_pos = self.coords_dict[char]
        return path

class Numpad(Pad):
    def __init__(self):
        layout = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            [None, '0', 'A']
        ]
        super().__init__(layout)

    def path_to_code(self, codes: str):
        cur_pos = self.coords_dict['A']
        path = ''
        for char in codes:
            path += self.shortest_path(cur_pos, self.coords_dict[char])
            cur_pos = self.coords_dict[char]
        return path

if __name__ == '__main__':
    numpad = Numpad()
    keypad = Keypad()

    solutions = {}

    with open('input', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            path = numpad.path_to_code(line)
            path = keypad.path_to_code(path, 25)
            solutions[line] = path
    
    answer = 0
    for entry in solutions:
        print(f"{entry}: {solutions[entry]}")
        answer += solutions[entry]*int(entry[:-1])
    print(f"Answer: {answer}")

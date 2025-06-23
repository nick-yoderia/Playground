import msvcrt
import os
from collections import defaultdict

class box:
    def __init__(self, y, x):
        self.y1, self.x1 = y,x
        self.y2, self.x2 = y,x+1

    def __eq__(self, coords: tuple):
        return coords == (self.y1, self.x1) or coords == (self.y2, self.x2)
    
    def can_move(self, dy, dx, walls):
        if (self.y1+dy, self.x1+dx) in walls or (self.y2+dy, self.x2+dx) in walls:
            return False
        return True

    def move (self, dy, dx, walls):
        if self.can_move(dy, dx, walls):
            self.y1, self.x1 = self.y1 + dy, self.x1 + dx
            self.y2, self.x2 = self.y2 + dy, self.x2 + dx

    @property
    def left(self):
        return self.y1, self.x1
    
    @property
    def right(self):
        return self.y2, self.x2



def load_data(input):
    with open(input, 'r') as file:
        data = file.read()
        warehouse, moves = data.split('\n\n')
        warehouse = warehouse.splitlines()
        warehouse = [line.strip() for line in warehouse]
        moves = moves.replace('\n', '').strip()
        MAXY, MAXX = len(warehouse), len(warehouse[0]*2)
    return warehouse, moves, MAXY, MAXX

def mapify(warehouse):
    walls = set()
    boxes = []
    for y in range(MAXY):
        for x in range(MAXX//2):
            if warehouse[y][x] == '#':
                walls.add((y,2*x))
                walls.add((y,2*x+1))
            elif warehouse[y][x] == 'O':
                boxes.append(box(y,2*x))
            elif warehouse[y][x] == '@':
                robot = (y, 2*x)
    return walls, boxes, robot

def move_robot(move: str, walls: set, boxes: set, robot):
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    dy, dx = moves[move]
    new_y = robot[0] + dy
    new_x = robot[1] + dx
    if 0 <= new_y < MAXY and 0 <= new_x < MAXX:
        if (new_y, new_x) not in boxes and (new_y, new_x) not in walls:
            robot = (new_y, new_x)
        elif (new_y, new_x) in boxes:
            if move_box((new_y, new_x), dy, dx, walls, boxes):
                robot = (new_y, new_x)
    return robot

def move_box(pos, dy, dx, walls, boxes):
    y, x = pos
    if not (0 <= y < MAXY and 0 <= x < MAXX):
        return False
    elif (y, x) not in boxes and (y, x) not in walls:
        return True
    elif (y, x) in walls:
        return False
    else:
        for cursor in boxes:
            if (y, x) == cursor:
                if move_box(tuple(map(sum,zip(cursor.left, (dy,dx)))), dy, dx, walls, boxes) \
                and move_box(tuple(map(sum,zip(cursor.right, (dy,dx)))), dy, dx, walls, boxes):
                    cursor.move(dy,dx, walls)

def draw_map(walls: set, boxes: set, robot, move):
    rows = []
    for y in range(MAXY):
        row = []
        x = 0
        while x < MAXX:
            if (y, x) in walls:
                row.append('#')
            elif (y, x) == robot:
                row.append('@')
            elif (y, x) in boxes:
                row.append('[')
                row.append(']')
                x += 1
            else:
                row.append('.')
            x += 1
        rows.append(''.join(row))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(rows))
    print(f"\nNext move: {move}\n")

if __name__ == '__main__':
    DEBUG = True
    warehouse, moves, MAXY, MAXX = load_data('input')
    walls, boxes, robot = mapify(warehouse)
    
    if DEBUG:
        for move in moves:
            draw_map(walls, boxes, robot, move)
            key = msvcrt.getch()
            if key == b'q':
                break
            else:
                robot = move_robot(move, walls, boxes, robot)
    else:
        for move in moves:
            robot = move_robot(move, walls, boxes, robot)
        sum = 0
        for box in boxes:
            sum += 100 * box[0] + box[1]
        print(sum)
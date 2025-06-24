import msvcrt
import os
import time

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
    boxes = set()
    for y in range(MAXY):
        for x in range(MAXX//2):
            if warehouse[y][x] == '#':
                walls.add((y,2*x))
                walls.add((y,2*x+1))
            elif warehouse[y][x] == 'O':
                boxes.add((y,2*x))
            elif warehouse[y][x] == '@':
                robot = (y, 2*x)
    return walls, boxes, robot

def move_robot(move: str, walls: set, boxes: set, robot):
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    dy, dx = moves[move]
    new_robot = robot
    new_y = robot[0] + dy
    new_x = robot[1] + dx
    new_boxes = set()
    if 0 <= new_y < MAXY and 0 <= new_x < MAXX:
        if (new_y, new_x) not in boxes and (new_y, new_x - 1) not in boxes and (new_y, new_x) not in walls:
            new_robot = (new_y, new_x)
        elif (new_y, new_x) in boxes:
            if dy == 0:
                if move_box_horizontal(new_y, new_x, dy, dx, walls, boxes):
                    new_robot = (new_y, new_x)
            else:
                if move_box_vertical(new_y, new_x, dy, dx, walls, boxes, new_boxes):
                    boxes.update(new_boxes)
                    new_robot = (new_y, new_x)
                else:
                    new_boxes = set((y-dy,x-dx) for y,x in new_boxes)
                    boxes.update(new_boxes)
        elif (new_y, new_x - 1) in boxes:
            if dy == 0:
                if move_box_horizontal(new_y, new_x - 1, dy, dx, walls, boxes):
                    new_robot = (new_y, new_x)
            else:
                if move_box_vertical(new_y, new_x - 1, dy, dx, walls, boxes, new_boxes):
                    boxes.update(new_boxes)
                    new_robot = (new_y, new_x)
                else:
                    new_boxes = set((y-dy,x-dx) for y,x in new_boxes)
                    boxes.update(new_boxes)
    return new_robot

def move_box_vertical(y, x, dy, dx, walls, boxes: set, new_boxes: set):
    move_flag = True
    if (y, x) not in boxes:
        return False
    
    cursor = (y, x)
    new_box = (y + dy, x + dx)
    ny, nx = new_box

    if not (0 <= ny < MAXY and 0 <= nx < MAXX):
        return False
    elif (ny, nx) in walls or (ny, nx + 1) in walls:
        return False
    elif (ny, nx) in boxes:
        move_flag = move_box_vertical(ny, nx, dy, dx, walls, boxes, new_boxes)
    if (ny, nx - 1) in boxes:
        move_flag = move_flag and move_box_vertical(ny, nx - 1, dy, dx, walls, boxes, new_boxes)
    if (ny, nx + 1) in boxes:
        move_flag = move_flag and move_box_vertical(ny, nx + 1, dy, dx, walls, boxes, new_boxes)

    boxes.remove(cursor)
    new_boxes.add(new_box)
    return move_flag

def move_box_horizontal(y, x, dy, dx, walls, boxes: set):
    move_flag = True
    if (y, x) not in boxes:
        return False
    
    cursor = (y, x)
    new_box = (y + dy, x + dx)
    ny, nx = new_box

    if not (0 <= ny < MAXY and 0 <= nx < MAXX):
        return False
    elif (ny, nx) in walls or (ny, nx + 1) in walls:
        return False
    elif (ny, nx+dx) in boxes:
        move_flag = move_box_horizontal(ny, nx+dx, dy, dx, walls, boxes)

    if move_flag:
        boxes.remove(cursor)
        boxes.add(new_box)
    return move_flag

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
    print(f"\n{robot}")
    print(f"Next move: {move}\n")

if __name__ == '__main__':
    DEBUG = False
    warehouse, moves, MAXY, MAXX = load_data('input')
    walls, boxes, robot = mapify(warehouse)
    
    if DEBUG:
        for move in moves:
            draw_map(walls, boxes, robot, move)
            key = msvcrt.getch()
            if key == b'\xe0':  # Special key prefix
                key = msvcrt.getch()  # Discard or handle second byte
            if key == b'q':
                break
            else:
                robot = move_robot(move, walls, boxes, robot)
        draw_map(walls, boxes, robot, move)
    else:
        for move in moves:
            robot = move_robot(move, walls, boxes, robot)
        sum = 0
        for box in boxes:
            sum += 100 * box[0] + box[1]
        print(sum)
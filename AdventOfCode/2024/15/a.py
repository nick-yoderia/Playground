import msvcrt
import os

def load_data(input):
    with open(input, 'r') as file:
        data = file.read()
        warehouse, moves = data.split('\n\n')
        warehouse = warehouse.splitlines()
        warehouse = [line.strip() for line in warehouse]
        moves = moves.replace('\n', '').strip()
        MAXY, MAXX = len(warehouse), len(warehouse[0])
    return warehouse, moves, MAXY, MAXX

def mapify(warehouse):
    walls = set()
    boxes = set()
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == '#':
                walls.add((y,x))
            elif warehouse[y][x] == 'O':
                boxes.add((y,x))
            elif warehouse[y][x] == '@':
                robot = (y, x)
    return walls, boxes, robot

def move_robot(move: str, walls: set, boxes: set, robot):
    moves = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<':(0,-1)}
    dy, dx = moves[move]
    y, x = robot
    y += dy
    x += dx
    if 0 < y <= MAXY or 0 <= x < MAXX:
        if (y, x) not in boxes and (y, x) not in walls:
            robot = (y,x)
        elif (y, x) in boxes:
            if move_box(y, x, dy, dx, walls, boxes):
                robot = (y, x)
                boxes.remove((y, x))
        return robot

def move_box(y, x, dy, dx, walls: set, boxes: set):
    if not (0 < y <= MAXY) or not (0 <= x < MAXX):
        return False
    elif (y,x) not in boxes and (y, x) not in walls:
        boxes.add((y,x))
        return True
    elif (y, x) in walls:
        return False
    else:
        return move_box(y+dy, x+dx, dy, dx, walls, boxes)

def draw_map(walls: set, boxes: set, robot, move):
    rows = []
    for i in range(MAXY):
        row = []
        for j in range(MAXX):
            if (i, j) in walls:
                row.append('#')
            elif (i, j) in boxes:
                row.append('O')
            elif (i, j) == robot:
                row.append('@')
            else:
                row.append('.')
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
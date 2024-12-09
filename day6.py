from colorama import Fore, Style, init
import copy

file = open("./inputs/input_d6")
file_stream = file.read()

lab = file_stream.split("\n")
lab.remove("")


four_directions = {
    "v" : [1,0],
    "<" : [0,-1],
    "^" : [-1,0],
    ">" : [0,1]
}

def copy_map(iterable):
    copy = []
    for line_index, line in enumerate(iterable):
        copy.append([])
        for char in line:
            copy[line_index].append([char])
    return copy

def find_guard(iterable):
    for height, line in enumerate(iterable):
        for width, char in enumerate(line):
            for guard_char in four_directions:
                if guard_char == char[0]:
                    return [height, width, guard_char]
    return False    


def change_guard_direction(iterable):
    y, x, dir_char = find_guard(iterable)
    direction_chars = list(four_directions.keys())
    dir_key_index = direction_chars.index(dir_char)
    new_dir = ""
    
    if dir_key_index == (len(direction_chars) - 1):
        new_dir = direction_chars[0]
    else:
        new_dir = direction_chars[dir_key_index + 1]
    iterable[y][x] = new_dir


def is_inbounds(y, x, iterable):
    if y < 0 or y >= len(iterable):
        print("Out of bounds on the Y axis. Trying to move to " + str(y))
        return False
    if x < 0 or x >= len(iterable[y]):
        print("Out of bounds on the X axis. Trying to move to " + str(x))
        return False
    return True


def move_guard(iterable):
    y, x, direction = find_guard(iterable)
    dir_vector = four_directions[direction]

    new_position_y = y + dir_vector[0]
    new_position_x = x + dir_vector[1]
    if not is_inbounds(new_position_y, new_position_x, iterable):
        return False

    iterable[y][x] = '.'
    iterable[new_position_y][new_position_x] = direction
    return True



#Part 1
lab_map = copy_map(lab)
patrol_map = copy_map(lab)

has_exited = False
while not has_exited:
    guard_y, guard_x, direction = find_guard(lab_map)
    patrol_map[guard_y][guard_x] = "X"
        
    next_tile_x = guard_x + four_directions[direction][1]
    next_tile_y = guard_y + four_directions[direction][0]

    if not is_inbounds(next_tile_y, next_tile_x, lab_map):
        has_exited = True
        continue

    next_tile_char = lab_map[next_tile_y][next_tile_x]
    if next_tile_char[0] == "#":
        change_guard_direction(lab_map)
    else:
            
        has_exited = not move_guard(lab_map)



#Print out for the patrol_map
for line in patrol_map:
    for char in line:
        if char[0] == "X":
            print(Fore.BLUE + str(char[0]) + Style.RESET_ALL, end="")
        else:
            print(char[0], end="")
    print("\n")

counter = 0
for line in patrol_map:
    for char in line:
        if char[0] == "X":
            counter += 1

print(counter)

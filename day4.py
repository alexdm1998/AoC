file = open("./inputs/input_d4")

input_string = file.read()
lines = input_string.split("\n")

message_grid = []
for index, line in enumerate(lines):
    line_chars = []
    if len(line) == 0:
        continue
    for char in line:
        line_chars.append(char)
    message_grid.append(line_chars)


def clamp_range(starting_value, ending_value, iterable):
    return range(max(starting_value, 0), min(ending_value, len(iterable)))



def find_next(y, x, direction_y, direction_x, letter):
    new_y = y + direction_y
    new_x = x + direction_x

    if new_y < 0 or new_y >= len(message_grid):
        return 0
    if new_x < 0 or new_x >= len(message_grid[new_y]):
        return 0
    if message_grid[new_y][new_x] == letter and letter == "A":
        return find_next(new_y, new_x, direction_y, direction_x, "S")
    if message_grid[new_y][new_x] == letter and letter == "S":
        return 1
    return 0


def find_m(y,x):

    counter = 0
    searchable_range_y = clamp_range(y-1, y+2, message_grid)
    for i in searchable_range_y:
        searchable_range_x = clamp_range(x-1, x+2, message_grid[i])
        for j in searchable_range_x:
            if message_grid[i][j] == "M":
                direction_y = i - y 
                direction_x = j - x
                counter += find_next(i, j, direction_y, direction_x, "A")
    return counter




def find_x(grid, func):
    counter = 0
    for line_index,line in enumerate(grid):
        for char_index, char in enumerate(line):
            if char == "X":
                counter += func(line_index, char_index)
    print(counter) #2685




#part 2
def verify_diagonals(y,x):
    if y == 0 or y == (len(message_grid) - 1):
        return 0
    if x == 0 or x == (len(message_grid[y]) - 1):
        return 0

    first_diagonal = False
    first_diagonal_char = message_grid[y-1][x-1]
    if first_diagonal_char == "M" or first_diagonal_char == "S":
        if message_grid[y+1][x+1] == "M" or message_grid[y+1][x+1] == "S":
            if first_diagonal_char != message_grid[y+1][x+1]:
                first_diagonal = True
    second_diagonal = False
    second_diagonal_char = message_grid[y-1][x+1]
    if second_diagonal_char == "M" or second_diagonal_char == "S":
        if message_grid[y+1][x-1] == "M" or message_grid[y+1][x-1] == "S":
            if second_diagonal_char != message_grid[y+1][x-1]:
                second_diagonal = True
    
    if first_diagonal and second_diagonal:
        return 1
    else:
        return 0



def find_ray(grid):
    counter = 0
    for line_index, line in enumerate(grid):
        for char_index, char in enumerate(line):
            if char == "A":
               counter += verify_diagonals(line_index, char_index)
    print(counter)


find_ray(message_grid)
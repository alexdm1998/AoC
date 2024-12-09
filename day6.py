file = open("./inputs/input_d6")
file_stream = file.read()

lab = file_stream.split("\n")
lab.remove("")

lab_map = []
for line in lab:
    line_array = []
    for char in line:
        line_array.append(char)
    lab_map.append(line_array)


#Part 1
n = len(lab_map)
m = len(lab_map[0])
cy, cx = 0,0
for height, string in enumerate(lab_map):
    for width, char in enumerate(string):
        if char in ["^",">", "v", ">"]:
            cy, cx = height, width

direcs = [[-1,0],[0,1],[1,0],[0,-1]]
cd = 0

historic = set()
while True:
    pcy = cy + direcs[cd][0]
    pcx = cx + direcs[cd][1]

    if pcy not in range(n) or pcx not in range(m):
        historic.add((cy,cx))
        break

    if lab_map[pcy][pcx] == "#":
        cd = (cd + 1) % 4
    else:
        historic.add((cy,cx))
        cy = pcy
        cx = pcx

counter = 0
for tile in historic:
    print(tile)
    counter += 1
print(counter)

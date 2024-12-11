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
icy, icx = 0,0
for height, string in enumerate(lab_map):
    for width, char in enumerate(string):
        if char in ["^",">", "v", ">"]:
            icy, icx = height, width

direcs = [[-1,0],[0,1],[1,0],[0,-1]]
icd = 0



history = set()
lcy, lcx, lcd = icy, icx, icd
while True:
    pcy = lcy + direcs[lcd][0]
    pcx = lcx + direcs[lcd][1]

    if pcy not in range(n) or pcx not in range(m):
        history.add((lcy,lcy))
        break

    if lab_map[pcy][pcx] == "#":
        lcd = (lcd + 1) % 4
    else:
        history.add((lcy, lcx))
        lcy = pcy
        lcx = pcx
counter = 0
for tile in history:
    counter += 1
print("####### Part 1 #######")
print(counter) #4758


counter = 0
for i in range(n):
    for j in range(m):
        historic = set()

        if not lab_map[i][j] == "#" and not lab_map[i][j] == "^":
            lab_map[i][j] = "#"
        else:
            continue

        cy, cx, cd = icy, icx, icd
        while True:
            pcy = cy + direcs[cd][0]
            pcx = cx + direcs[cd][1]
            
            if pcy not in range(n) or pcx not in range(m):
                break

            tile = (pcy, pcx, cd)
            if tile in historic:
                counter += 1
                break

            if lab_map[pcy][pcx] == "#":
                historic.add((cy, cx, cd))
                cd = (cd + 1) % 4
            else:
                cy = pcy
                cx = pcx

        lab_map[i][j] = "."
print("##### Part 2 ######")
print(counter) #1670

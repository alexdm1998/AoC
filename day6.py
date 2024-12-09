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



counter = 0
for i in range(n):
    for j in range(m):
        print("Checking at: (" + str(i) + "," + str(j) + ")")
        print("Current counter of obstacles: " + str(counter))

        historic = set()

        if not lab_map[i][j] == "#" or not lab_map[i][j] == "^":
            lab_map[i][j] = "#"
        else:
            continue

        while True:
            pcy = cy + direcs[cd][0]
            pcx = cx + direcs[cd][1]
        
            if pcy not in range(n) or pcx not in range(m):
                break
            
            next_tile = (cy, cx, cd)
            if next_tile in historic:
                counter += 1
                break
            
            if lab_map[pcy][pcx] == "#":
                historic.add((cy,cx,cd))
                cd = (cd + 1) % 4
            else:
                cy = pcy
                cx = pcx
        
        lab_map[i][j] = "."
        
print(counter)








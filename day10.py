file = open("./inputs/input_d10")
filestream = file.read()


input_map = filestream.split("\n")
input_map.remove("")


#Construction of topographic map n * m
topographic_map = []

for line in input_map:
    topographic_map.append(list(map(int, line)))


n = len(topographic_map)
m = len(topographic_map[0])


directions = [[-1,0], [1, 0], [0, 1], [0, -1]]




def next_elevation(y,x, collector):
    for direction in directions:
        current_tile = topographic_map[y][x]

        if current_tile == 9:
            collector.add((y, x))
        if not (y + direction[0]) in range(n) or not (x + direction[1]) in range(m):
            continue

        next_tile = topographic_map[y + direction[0]][x + direction[1]]
        if next_tile <= current_tile:
            continue
        if next_tile == current_tile + 1:
            next_elevation(y + direction[0], x + direction[1], collector)
        

#Part 1
counter = 0
for y in range(n):
    for x in range(m):
        if topographic_map[y][x] == 0:
            destination_collector = set()
            next_elevation(y,x, destination_collector)
            for destination in destination_collector:
                counter += 1

print("####### Part 1 #######")
print(counter) #538



#Part 2
def next_elevation_rating(y,x, collector):
    for direction in directions:
        current_tile = topographic_map[y][x]
        if not (y + direction[0]) in range(n) or not (x + direction[1]) in range(m):
            continue

        next_tile = topographic_map[y + direction[0]][x + direction[1]]
        
        if next_tile == 9 and current_tile == 8:
            collector[0] += 1
        if next_tile <= current_tile:
            continue
        if next_tile == current_tile + 1:
            next_elevation_rating(y + direction[0], x + direction[1], collector)


print("####### Part 2 ######")
counter = 0
for y in range(n):
    for x in range(m):
        if topographic_map[y][x] == 0:
            rating_collector = [0]
            next_elevation_rating(y, x, rating_collector)
            counter += rating_collector[0]


print(counter)


            

file = open("./inputs/input_d8")
file_stream = file.read()
antenna_map = file_stream.split("\n")
antenna_map.remove("")




n = len(antenna_map)
m = len(antenna_map[0])
antenna_dict = {}
antinode_set = set()
#Part 1
for y, line in enumerate(antenna_map):
    for x, char in enumerate(line):
        if char == '.':
            continue

        antennas = list(antenna_dict.keys())
        if char not in antennas:
            antenna_dict[char] = [[y, x]]
        else:
            antenna_dict[char].append([y,x])


for key in list(antenna_dict.keys()):
    antenna_list = antenna_dict[key] 
    
    for index, antenna in enumerate(antenna_list):
        antenna_sublist = antenna_list[:index] + antenna_list[index+1:]
        for sibling_index, sibling_antenna in enumerate(antenna_sublist):
            distance_vector = [antenna[0] - sibling_antenna[0], antenna[1] - sibling_antenna[1]]
            antinode = (antenna[0] + distance_vector[0], antenna[1] + distance_vector[1])
            if antinode[0] in range(n) and antinode[1] in range(m):
                antinode_set.add(antinode)

counter = 0
for antinode in antinode_set:
    counter += 1
print("########## Part 1 ##########")
print(counter) #394

#Part 2
antinode_set = set()


for key in list(antenna_dict.keys()):
    antenna_list = antenna_dict[key]


    for index, antenna in enumerate(antenna_list):
        antenna_sublist = antenna_list[:index] + antenna_list[index+1:]
        for sibling_index, sibling_antenna in enumerate(antenna_sublist):
            distance_vector = [antenna[0] - sibling_antenna[0], antenna[1] - sibling_antenna[1]]
            antinode = (antenna[0] - distance_vector[0], antenna[1] - distance_vector[1])
            while antinode[0] in range(n) and antinode[1] in range(m):
                antinode_set.add(antinode)

                antinode = (antinode[0] - distance_vector[0], antinode[1] - distance_vector[1])

counter = 0
for antinode in antinode_set:
    counter += 1
print("########## Part 2 ##########")
print(counter) #1277

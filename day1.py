#Part 1
distance_total = 0


left_list = []
right_list = []
with open("./inputs/input_d1", "r") as file:
    for line in file:
        split_string = line.split()
        left_list.append(int(split_string[0]))
        right_list.append(int(split_string[1]))


sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

for left_number, right_number in zip(sorted_left_list, sorted_right_list):
    distance = abs(right_number - left_number)
    distance_total += distance


print("#########################################")
print("########### Distance Total ##############")
print(distance_total)


#Part 2
similarity_score = 0

for left_number in sorted_left_list:
    for right_number in sorted_right_list:
        if left_number > right_number:
            continue
        if left_number == right_number:
            similarity_score += left_number

print("\n\n")
print("#########################################")
print("########## Similarity Score #############")
print(similarity_score)

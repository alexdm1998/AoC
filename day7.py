file = open("./inputs/input_d7")
file_stream = file.read()

input_table = file_stream.split("\n")
input_table.remove("")


equations = []
for string in input_table:
    split_string = string.split(":") 
    target = int(split_string[0])
    sequence = [int(item) for item in split_string[1].split(" ") if item != ""]
    equations.append([target, sequence])


#Part 1
def binary_permutate(target, sequence):
    n_permutations = pow(2, len(sequence) - 1)
    is_valid = False

    for i in range(n_permutations):
        mask_divider = 1
        total = 0
        
        for index, number in enumerate(sequence):
            if index == 0:
                total = number
                continue

            mask = i // mask_divider
            operation = mask % 2
            if operation == 0:
                total = total + number
            else:
                total = total * number

            mask_divider *= 2
        if total == target:
            is_valid = True
    if is_valid:
        return target
    else:
        return 0

#Part 2
def ternary_permutate(target, sequence):
    n_permutations = pow(3, len(sequence) - 1)
    is_valid = False

    for i in range(n_permutations):
        mask_divider = 1

        total = 0
        for index, number in enumerate(sequence):
            if index == 0:
                total = number
                continue
            
            mask = i // mask_divider
            operation = mask % 3

            if operation == 0:
                total = total + number
            if operation == 1:
                total = total * number
            if operation == 2:
                total = int(str(total) + str(number))

            mask_divider *= 3

        if total == target:
            is_valid = True

    if is_valid:
        return target
    else:
        return 0


counter_part_1 = 0
counter_part_2 = 0
for index, equation in enumerate(equations):
    target = equation[0]
    sequence = equation[1]

    counter_part_1 += binary_permutate(target, sequence)
    counter_part_2 += ternary_permutate(target, sequence)

print("######### Part 1 ##########")
print(counter_part_1) #1260333054159
print("######### Part 2 ##########")
print(counter_part_2) #162042343638683

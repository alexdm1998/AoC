import copy
file = open("./inputs/input_d9")
file_stream = file.read()


storage = []
id = 0
for index, number in enumerate(file_stream):
    if number.isdigit():
        if index % 2 == 0:
            for file_index in range(int(number)):
                storage.append(id)
            id += 1
        if index % 2 == 1:
            for file_index in range(int(number)):
                storage.append(".")


storage_copy = copy.deepcopy(storage)


end_index = 0
for index, item in enumerate(storage):
    if type(item) == int:
        continue
    

    while end_index in range(len(storage)):
        if index >= (len(storage)-1-end_index):
            break
        end_item = storage[len(storage) - 1 - end_index]
        if not type(end_item) == int:
            end_index += 1
            continue
        else:
            storage[index] = end_item 
            storage[len(storage) - 1 - end_index] = "."
            break


counter = 0
for index, item in enumerate(storage):
    if type(item) == int:
        counter += index * item
print("######### Part 1 #######")
print(counter) #6398608069280

#Part 2
n = len(storage_copy)
search_id = None
block_length = 0
back_index = 0
while back_index < n:
    back_item = storage_copy[n - 1 - back_index]
    if block_length == 0 and type(back_item) != int:
        back_index += 1
        continue
    if search_id == None and type(back_item) == int:
        search_id = back_item
        block_length += 1
        back_index += 1
        continue
    if search_id == back_item:
        block_length += 1
        back_index += 1
        continue
    if search_id != back_item:
        back_index -= 1
        space_length = 0
        for front_index in range(n):
            front_item = storage_copy[front_index]
            
            if front_index > (n - 1 - back_index):
                block_length = 0
                search_id = None
                break
            if front_item == ".":
                space_length += 1
            else:
                space_length = 0
            if space_length == block_length:
                for offset in range(block_length):
                    storage_copy[front_index - offset] = storage_copy[n - 1 - back_index + offset]
                    storage_copy[n - 1 - back_index + offset] = "."
                block_length = 0
                search_id = None
                break
        back_index += 1



counter = 0
for index, item in enumerate(storage_copy):
    if type(item) == int:
        counter += index * item
print("########## Part 2 ########")
print(counter) #6427437134372


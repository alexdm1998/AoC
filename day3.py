import re
#Importing inputs
file = open("./inputs/input_d3")
input_string = file.read()



#Part 1
def find_muts(string):
    finds = re.findall(r"mul\(\d{1,3},\d{1,3}\)", string)
    return finds

def multiply_mut(mut):
    numbers = re.findall(r"\d{1,3}", mut)
    multiplication = int(numbers[0]) * int(numbers[1])
    return multiplication


total = 0
found_muts = find_muts(input_string)
total += sum(multiply_mut(m) for m  in found_muts)
print("########## Part 1 ###########")
print(total) #168,539,636

#Part 2
def has_donts(string):
    if string.find("don't()") != -1:
        return True
    return False


def string_pruner(string):
    substring = string
    valid_segments = []

    if not has_donts(substring):
        return substring
    while has_donts(substring):
        last_index = substring.find("don't()")
        valid_segments.append(substring[:last_index])
        substring = substring[last_index+7:]
        #Next segment
        starting_index = substring.find("do()")
        if starting_index == -1:
            return valid_segments
        substring = substring[starting_index:]
    valid_segments.append(substring)
    return valid_segments
        


total = 0
pruned_string_list = string_pruner(input_string)
pruned_string = "".join(pruned_string_list)
muts = find_muts(pruned_string)
total += sum(multiply_mut(m) for m in muts)

print("\n\n########## Part 2 ###########")
print(total) #97,529,391
            
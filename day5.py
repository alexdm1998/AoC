file = open("./inputs/input_d5")

stream = file.read()
sections = stream.split("\n\n")

#print("####### Section 1 ########")
update_orders = sections[0].split("\n")

ruleset = {}
for update_order in update_orders:
    versions = update_order.split("|")
    predecessor = versions[0]
    sucessor = versions[1]


    if predecessor not in ruleset:
        ruleset[predecessor] = [sucessor]
    else:
        ruleset[predecessor].append(sucessor)



def check_predecessors(search_value, iterator):
    for item in iterator:
        for ruleset_value in ruleset[item]:
            if ruleset_value == search_value:
                return False
    return True

def check_sucessors(search_value, iterator):
    for item in iterator:
        for ruleset_value in ruleset[search_value]:
            if ruleset_value == item:
                return False
    return True

def check_ruleset(item, log_list):
    item_index = log_list.index(item)
    if not check_predecessors(item, log_list[item_index+1:]):
        return False
    if not check_sucessors(item, log_list[:item_index]):
        return False
    return True

def middle_value(iterator):
    length = len(iterator)
    return iterator[int((length-1)/2)]

#print("####### Section 2 ########")
updates_log = sections[1].split("\n")


counter = 0
for update_log in updates_log:
    should_count = True
    if update_log == "":
        continue
    log_list = update_log.split(",")
    for update in log_list:
        if check_ruleset(update, log_list) == False:
            should_count = False
            break

    if should_count:
        counter += int(middle_value(log_list))

print(counter) #5108



#Part 2
def is_fixed(log_list):
    for update in log_list:
        if check_ruleset(update, log_list) == False:
            return False
    return True


def fix_list(log_list):
    while not is_fixed(log_list):
        for index, update in enumerate(log_list):
            for other_update in log_list[index + 1:]:
                if update in ruleset[other_update]:
                    update_index = log_list.index(update)
                    other_update_index = log_list.index(other_update)
                    log_list[update_index] = other_update
                    log_list[other_update_index] = update
    
counter = 0
for update_log in updates_log:
    should_count = False
    if update_log == "":
        continue
    log_list = update_log.split(",")
    for update in log_list:
        if check_ruleset(update, log_list) == False:
            should_count = True
            break
    if should_count:
        fix_list(log_list)
        counter += int(middle_value(log_list))




print(counter) #7380

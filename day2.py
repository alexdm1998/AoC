import math


levels = []
with open("./inputs/input_d2", "r") as file:
    for level in file:
        split_level = level.split()
        parsed_level = [int(number) for number in split_level]
        levels.append(parsed_level)


def evaluate_safety(level):
    previous_number = None
    difference_signal = None

    for index, number in enumerate(level):
        if not previous_number:
            previous_number = number
            continue
        difference = previous_number - number
        if not difference_signal:
            difference_signal = math.copysign(1, difference)
        if difference_signal != math.copysign(1, difference):
            return 0
        if abs(difference) == 0 or abs(difference) > 3:
            return 0
        if index == (len(level) - 1):
            return 1
        previous_number = number

safety = 0
for level in levels:
    eval_value = evaluate_safety(level)
    if eval_value:
        safety += eval_value
    else:
        for index, number in enumerate(level):
            new_level = level[:index] + level[index + 1:]
            if evaluate_safety(new_level):
                safety += evaluate_safety(new_level)
                break
print(safety)


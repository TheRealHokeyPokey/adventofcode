import numpy as np

lines = []
with open('input') as input:
    lines = input.readlines()
        
safe = 0
for line in lines:
    list_line = [int(ele) for ele in line.strip().split(sep=" ")]

    for i in range(len(list_line) + 1):

        this_list = list_line.copy()
        if i != len(list_line):
            this_list.pop(i)

        diff_list = [a-b for a, b in zip(this_list, this_list[1:])]

        if any(3 < abs(ele) or abs(ele) < 1 for ele in diff_list):
            continue
        if any(np.sign(ele) != np.sign(diff_list[0]) for ele in diff_list):
            continue
        safe += 1
        break


print(f'{safe=}')



import numpy as np

lines = []
with open('input') as input:
    lines = input.readlines()
        
safe = 0
for line in lines:
    list_line = [int(ele) for ele in line.strip().split(sep=" ")]

    diff_list = []
    for a, b in zip(list_line, list_line[1:]):
        diff_list.append(a-b)
    if any(3 < abs(ele) or abs(ele) < 1 for ele in diff_list):
        continue
    if any(np.sign(ele) != np.sign(diff_list[0]) for ele in diff_list):
        continue
    safe += 1

print(f'{safe=}')



with open('input') as input:
    data = input.readlines()

target = 'MAS'
count = 0

for l_i, line in enumerate(data):
    data[l_i] = data[l_i].strip()

for l_i, line in enumerate(data):
    if l_i == 0: continue # if first line
    if l_i + 1 == len(data): continue # if last line

    for e_i, ele in enumerate(line):
        if ele != 'A': continue # if wrong character
        if e_i + 1 == len(line): continue # if character last in line
        if e_i == 0: continue # if character first in line

        test_1 = "".join([data[l_i-1][e_i-1], data[l_i][e_i], data[l_i+1][e_i+1]])
        test_2 = "".join([data[l_i-1][e_i+1], data[l_i][e_i], data[l_i+1][e_i-1]])

        if (test_1 == target or test_1 == "".join(reversed(target))) and (test_2 == target or test_2 == "".join(reversed(target))):
            count += 1

print(f'{count=}')


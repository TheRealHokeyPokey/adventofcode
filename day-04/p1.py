

with open('input') as input:
    data = input.readlines()


def check_test(in_string):
    if in_string == target or in_string == "".join(reversed(target)):
        return True
    else:
        return False

target = 'XMAS'
count = 0

for l_i, line in enumerate(data):
    line = line.strip()

    for e_i, ele in enumerate(line):
 
        if len(line) > e_i + 3:
            test = line[e_i:e_i + 4]
            if check_test(test):
                count += 1

        if len(data) > l_i + 3:
            test = "".join([data[y][x] for y, x in zip(range(l_i, l_i+4), [e_i]*4)])
            if check_test(test):
                count += 1

        if len(data) > l_i + 3 and len(line) > e_i + 3:
            test = "".join([data[y][x] for y, x in zip(range(l_i, l_i+4), range(e_i, e_i+4))])
            if check_test(test):
                count += 1

        if len(data) > l_i + 3 and 0 <= e_i - 3:
            test = "".join([data[y][x] for y, x in zip(range(l_i, l_i+4), range(e_i, e_i-4, -1))])
            if check_test(test):
                count += 1

print(f'{count=}')


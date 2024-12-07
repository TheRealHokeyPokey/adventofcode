import re

with open('input') as input:
    data = input.read()

p = re.compile('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
m = p.findall(data)

total = 0
do_mult = True

for s in m:
    if s == "do()":
        do_mult = True
    elif s == "don't()":
        do_mult = False
    elif s[:4] == 'mul(':
        pair = s[4:][:-1].split(sep=',')
        if do_mult:
            total += int(pair[0]) * int(pair[1])

print(f'{total=}')
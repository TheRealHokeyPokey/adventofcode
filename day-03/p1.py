import re

with open('input') as input:
    data = input.read()

p = re.compile('mul\(\d{1,3},\d{1,3}\)')
m = p.findall(data)

total = 0
for s in m:
    pair = s[4:][:-1].split(sep=',')
    total += int(pair[0]) * int(pair[1])

print(f'{total=}')
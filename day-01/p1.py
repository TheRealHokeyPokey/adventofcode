with open('input') as input:
    input_lines = input.readlines()

a = []
b = []

for line in input_lines:
    a.append(int(line.strip().split()[0]))
    b.append(int(line.strip().split()[1]))

sum_diff = 0
while len(a) != 0 and len(b) != 0:
    min_a = min(a)
    min_b = min(b)
    sum_diff += abs(min_a - min_b)
    a.remove(min_a)
    b.remove(min_b)

print(sum_diff)
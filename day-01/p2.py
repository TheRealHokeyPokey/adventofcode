with open('input') as input:
    input_lines = input.readlines()

a = []
b = []

for line in input_lines:
    a.append(int(line.strip().split()[0]))
    b.append(int(line.strip().split()[1]))

sum_sim = 0
for ele in a:
    sum_sim += ele*b.count(ele)

print(sum_sim)
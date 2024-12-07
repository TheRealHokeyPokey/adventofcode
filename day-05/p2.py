import functools

cmp_tbl = dict()

def cmp_numbers(a, b):
    if b in cmp_tbl[a]:
        return -1
    else:
        return 1

with open('input') as input:
    data = input.readlines()

rules = []
pages = []

after_split = False
for index, line in enumerate(data):
    data[index] = data[index].strip()
    if not after_split:
        if line == '\n':
            after_split = True
            continue
        rules.append(data[index].split(sep='|'))
    else:
        pages.append(data[index].split(sep=','))

for rule in rules:
    cmp_tbl[rule[0]] = list()
for rule in rules:
    cmp_tbl[rule[0]].append(rule[1])

sum = 0
for page in pages:
    page_validity = True
    for rule in rules:
        if rule[0] not in page or rule[1] not in page:
            continue
        if page.index(rule[0]) >= page.index(rule[1]):
            page_validity = False
            break
    if not page_validity:
        sorted_page = sorted(page, key=functools.cmp_to_key(cmp_numbers))
        sum += int(sorted_page[len(sorted_page)//2])

print(f'{sum=}')
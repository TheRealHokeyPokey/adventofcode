with open('input') as input:
    data = input.readlines()

after_split = False

rules = []
pages = []

for index, line in enumerate(data):
    data[index] = data[index].strip()
    if not after_split:
        if line == '\n':
            after_split = True
            continue
        rules.append(data[index].split(sep='|'))
    else:
        pages.append(data[index].split(sep=','))

def val_index(page, val):
    if val in page:
        return page.index(val)
    else:
        return None

sum = 0

for page in pages:
    page_validity = True
    for rule in rules:
        if rule[0] not in page or rule[1] not in page:
            continue
        if page.index(rule[0]) >= page.index(rule[1]):
            page_validity = False
            break
    if page_validity:
        sum += int(page[len(page)//2])

print(f'{sum=}')







# import to plot path
#import matplotlib.pyplot as plt

with open('input') as input:
    data = input.read()
data = data.split(sep='\n')

def move_in_dir(coords, direction):
    x, y = coords
    if direction == 0: # up
        return (x, y-1)
    if direction == 1: # right
        return (x+1, y)
    if direction == 2: # down
        return (x, y+1)
    if direction == 3: # left
        return (x-1, y)
    else:
        return None

pos = []
x, y = None, None

for line_i, line in enumerate(data):
    if '^' in line:
        x = line.index('^')
        y = line_i
        break

dir = 0 # up
while len(data[0]) > x >= 0 and len(data) > y >= 0:

    pos.append((x, y))
    n_x, n_y = move_in_dir((x, y), dir)

    if len(data[0]) > n_x >= 0 and len(data) > n_y >= 0:
        if data[n_y][n_x] == '#':
            dir = (dir+1) % 4
    x, y = move_in_dir((x, y), dir)

print(len(set(pos)))

# code to plot the path
# warning, slow

# for e in pos:
#     plt.scatter(x=e[1], y=e[0])
# plt.show()

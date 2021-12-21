data = open('day13input.txt', 'r').read().split('\n')[:-1]
x = data.index('')
instructions = [[i.split('=')[0][-1], int(i.split('=')[1])] for i in data[(x+1):]]
data = [[int(j) for j in i.split(',')] for i in data[:x]]
#print(len(data), data, instructions)

for j in instructions:
    coord = j[0] == 'y'
    for i in data:
        if i[coord] > j[1]:
            i[coord] = 2 * j[1] - i[coord]
    n, data = data, []
    for i in n:
        if i not in data: data.append(i)

graph = []
for i in range(max([k[1] for k in data])+1):
    graph.append([])
    for j in range(max([k[0] for k in data])+1):
        if [j, i] in data: graph[i].append('#')
        else: graph[i].append('.')
for i in graph: print(''.join(i))
print('BLKJRBAG')
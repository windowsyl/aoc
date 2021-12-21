data = open('day15input.txt', 'r').read().split('\n')[:-1]
data = [[int(i) for i in j] for j in data]

maxy = len(data)
maxx = len(data[0])

for i in range(4):
    data = [i+[j+1 for j in i[-maxx:]] for i in data]
for i in range(4):
    data += [[j+1 for j in i] for i in data[-maxy:]]

data = [[j if j<10 else j-9 for j in i] for i in data]

maxy = len(data)
maxx = len(data[0])

Q = [(i, j) for i in range(maxy) for j in range(maxx)]
dists = {i:float('inf') for i in Q}
dists.pop((0,0))
Q.pop(0)
dists[(0,1)] = data[0][1]
dists[(1,0)] = data[1][0]

paths = {}

while Q:
    u = Q[0]
    for i in Q[1:]:
        if dists[i] < dists[u]: u = i

    if u == (maxy-1, maxx-1):
        print(dists[u])
        break

    #print(Q.pop(Q.index(u)))
    Q.pop(Q.index(u))
    for i in [[1,0], [0,1], [-1,0], [0,-1]]:
        v = (u[0]+i[0], u[1]+i[1])
        try:
            alt = dists[u] + data[v[0]][v[1]]
            if alt < dists[v]:
                dists[v] = alt
                paths[v] = u
        except (IndexError, KeyError):
            continue

# v = (maxy-1, maxx-1)
# print(v, data[v[0]][v[1]])
# while True:
#     v = paths[v]
#     print(v, data[v[0]][v[1]])
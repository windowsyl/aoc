data = open('day15inputexample.txt', 'r').read().split('\n')[:-1]
data = [[int(i) for i in j] for j in data]

maxy = len(data)
maxx = len(data[0])




def dijkstra(data):
    Q = [[i, j] for i in range(maxx) for j in range(maxy)]
    dist = [[],[]] #[locations[], dists[]]
    for i in range(maxx):
        for j in range(maxy):
            dist[0].append([i,j])
            dist[1].append(99999)
    
    dist[1].pop(dist[0].index([0,0]))
    dist[0].pop(dist[0].index([0,0]))
    Q.pop(Q.index([0,0]))

    dist[1][dist[0].index([0,1])] = data[1][0] #coords :<
    dist[1][dist[0].index([1,0])] = data[0][1]

    while Q:
        qdists = [dist[1][i] if dist[0][i] in Q else 99999999 for i in range(len(dist[1])) ]
        u = dist[0][dist[1].index(min(qdists))]
        Q.pop(Q.index(u))

        if u == [maxx, maxy]:
            return dist[1][dist[0].index[u]]

        for i in [[1,0], [0,1], [-1,0], [0,-1]]:
            v = [u[0]+i[0], u[1]+i[1]]
            try:
                alt = dist[1][dist[0].index(u)] + data[v[0]][v[1]]
                if alt < dist[1][dist[0].index(v)]: dist[1][dist[0].index(v)] = alt
            except ValueError:
                continue

dijkstra(data)




print(dijkstra(data))
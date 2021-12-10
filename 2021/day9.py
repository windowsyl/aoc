data = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678\n".split('\n')[:-1]
data = open('day9input.txt', 'r').read().split('\n')[:-1]
data = [[9]+[int(i) for i in j]+[9] for j in data]
data = [[9]*len(data[0])]+data+[[9]*len(data[0])]

#print(data)
risk = 0
for i in range(1, len(data)-1): #loop through all but edges
    for j in range(1, len(data[0])-1):
        if data[i][j] < data[i-1][j] and data[i][j] < data[i+1][j]:
            if data[i][j] < data[i][j-1] and data[i][j] < data[i][j+1]:
                risk += data[i][j]+1
print(risk)
basins = []

def floodthing(i, j):
    size = 1
    data[i][j]='a'
    if data[i-1][j] in range(9): size += floodthing(i-1,j)
    if data[i+1][j] in range(9): size += floodthing(i+1,j)
    if data[i][j-1] in range(9): size += floodthing(i,j-1)
    if data[i][j+1] in range(9): size += floodthing(i,j+1)
    return size



for i in range(1, len(data)-1): #loop through all but edges
    for j in range(1, len(data[0])-1):
        if data[i][j] in range(9):
            basins.append(floodthing(i, j))
basins.sort()
print(basins[-3]*basins[-2]*basins[-1])

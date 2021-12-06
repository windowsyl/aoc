data = 0
with open('day6input.txt', 'r') as f: data = f.read().split('\n')[:-1]
data = [i.split(' through ') for i in data]

codes = ['toggle ', 'turn off ', 'turn on ']
for i in range(len(data)):
    data[i][1] = [int(k) for k in data[i][1].split(',')]
    for j in range(len(codes)):
        if codes[j] in data[i][0]:
            data[i] = [['t','f','n'][j], [int(k) for k in data[i][0][len(codes[j]):len(codes[j])+7].split(',')], data[i][1]]

bigArray = [[0 for i in range(1000)] for j in range(1000)]
bigArrayp2 = [[0 for i in range(1000)] for j in range(1000)]
for i in data:
    x1 = i[1][0]
    x2 = i[2][0]
    y1 = i[1][1]
    y2 = i[2][1]
    if i[0] == 't':
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                bigArray[x][y] = 1-bigArray[x][y]
                bigArrayp2[x][y] += 2
    elif i[0] == 'f':
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                bigArray[x][y] = 0
                bigArrayp2[x][y] = max(bigArrayp2[x][y]-1, 0)
    elif i[0] == 'n':
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                bigArray[x][y] = 1
                bigArrayp2[x][y] += 1

countp1 = 0
countp2 = 0
for x in range(len(bigArray)):
    for y in range(len(bigArray[0])):
        countp1 += bigArray[x][y]
        countp2 += bigArrayp2[x][y]
print('p1:', countp1)
print('p2:', countp2)


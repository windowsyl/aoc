data = open('day5input.txt', 'r').read().split('\n')
#data = "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2".split('\n')
data = [i.split(' -> ') for i in data if i]
data = [[i[0].split(','), i[1].split(',')] for i in data]
data = [[[int(k) for k in j] for j in i] for i in data]

for i in data: print(i)
#[[[x1, y1], [x2, y2]], [], [],...]


bigArray = [[0 for i in range(1000)] for j in range(1000)]
for i in data:
    x1 = i[0][0]
    y1 = i[0][1]
    x2 = i[1][0]
    y2 = i[1][1]
    if x1 == x2:
        if y1 < y2:
            print('1:', i)
            for y in range(y1,y2+1):
                bigArray[x1][y]+=1
        else:
            print('2:', i)
            for y in range(y2,y1+1):
                bigArray[x1][y]+=1
    elif y1 == y2:
        if x1 < x2:
            print('3:', i)
            for x in range(x1,x2+1):
                bigArray[x][y1]+=1
        else:
            print('4:', i)
            for x in range(x2,x1+1):
                bigArray[x][y1]+=1
    else: print(i)


count = 0
sum = 0
for i in bigArray:
    for j in i:
        if j > 1:
            count+=1
        sum+=j
print(bigArray)
print(count, sum)
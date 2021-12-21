data = open('day11input.txt', 'r').read().split()

data = [['a']*(len(data)+2)]+[['a']+[int(i) for i in j]+['a'] for j in data]+[['a']*(len(data)+2)]
#for i in data: print(i)

count = 0
def flash(data, i, j):
    if data[i][j] == 'a' or data[i][j] == 'f': return
    data[i][j] += 1
    if data[i][j] > 9:
        data[i][j] = 'f'
        for inew in range(i-1, i+2):
            for jnew in range(j-1,j+2):
                    flash(data, inew, jnew)
                    
for a in range(100):
    for i in range(1,len(data)-1):
        for j in range(1,len(data[1])-1):
            flash(data, i, j)
    for i in range(1,len(data)-1):
        for j in range(1,len(data[1])-1):
            if data[i][j] == 'f':
                count += 1
                data[i][j]=0
            elif data[i][j] > 9: print(i, j, 'uh oh')
print(count)


#for i in data[1:-1]: print(i[1:-1])
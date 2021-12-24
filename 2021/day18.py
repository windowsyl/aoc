def send(x, dir, val, i):
    i += dir
    while not x[i].isnumeric():
        if i > 1 and i < len(x)-1: i+=dir
        else: break
    else: #you can't while elif??
        if i+dir > 1 and i+dir < len(x):
            if x[i+dir].isnumeric():
                x[min(i, i+dir):1+max(i, i+dir)] = list(str(int(''.join(x[min(i, i+dir):1+max(i, i+dir)])) + val))
                return
            insert = str(int(x[i])+val)
            x[i] = insert[-1]
            if len(insert)>1:
                x.insert(i, insert[0])    

def explode(x, y, i):
    length = y.index(']')+1
    left, right = ''.join(x[i:i+length][1:-1]).split(',')
    x[i:i+length] = '0'
    
    send(x, 1, int(right), i)
    send(x, -1, int(left), i)

    return x

def tryExplode(x):
    y = list(x)
    counter = 0
    i = 0
    while y and (counter < 4 or y[0] != '['):
        if y[0] == '[': counter += 1
        elif y[0] == ']': counter -= 1
        y.pop(0)
        i += 1
    if y:
        while y[1] == '[':
            y.pop(0)
            i+=1
        return explode(x, y, i)
    else: return False

def split(x, i):
    v = int(''.join(x[i:i+2]))
    insert = list(str([round(v/2-0.49), round(v/2+0.49)]))
    x[i:i+2] = insert
    # print(insert, insert[-2:], insert[:-2][::-1])
    # for j in insert[:-2][::-1]:
    #    x.insert(i, j)
    return x

def trySplit(x):
    for i in range(len(x)-1):
        if x[i].isnumeric() and x[i+1].isnumeric():
            return split(x, i)
    return False
        

def simplify(x):
    while True:
        #print('start:', ''.join(x))
        a = tryExplode(x)
        if a:
            x = a
            continue
        
        a = trySplit(x)
        if a: x = a
        else: break

    return ''.join(x)
    

def add(x, y):
    return simplify(list('['+x+','+y+']'))

def magnitude(x):
    if x.isnumeric(): return int(x)
    y = x[1:-1]
    count = 0
    for i in range(len(y)):
        if y[i] == '[': count+=1
        elif y[i] == ']': count-=1
        elif y[i] == ',' and count == 0:
            return 3*magnitude(y[:i])+2*magnitude(y[i+1:])

a = open('day18input.txt', 'r').read().split('\n')

sum = a[0]
for y in a[1:]:
    sum = add(sum, y).replace(' ', '')#idk how they get in
print('p1:', magnitude(sum))

mags = [0]
for i in range(len(a)):
    for j in range(len(a)):
        c = magnitude(add(a[i],a[j]).replace(' ',''))
        if c > max(mags):
            print(c, i, j)
            mags.append(c)





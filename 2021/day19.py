data = open('day19input.txt', 'r').read().split('---')
data = [[j for j in i.split('\n') if j] for i in data][1:]
for i in range(0, int(len(data)/2)):
    data.pop(i)
for i in range(len(data)):
    data[i] = [[int(k) for k in j.split(',')] for j in data[i]]
def checkScanners(a, b):
    for a1 in a[:-11]:
        for b1 in b:
            ac = a.copy()
            ac.remove(a1)
            bc = b.copy()
            bc.remove(b1)
            bloc = [a1[0]+b1[0], a1[1]+b1[1], a1[2]+b1[2]]
            countAligned = 0
            for a2 in ac:
                for b2 in bc:
                    if [a2[0]+b2[0], a2[1]+b2[1], a2[2]+b2[2]] == bloc:
                        countAligned+=1
                        #print(a1, b1, a2, b2, countAligned, bloc)
                        bc.remove(b2)
                        break
                if countAligned >= 11: return bloc

def rotateflip(data, r, f):
    data = data.copy()
    for i in range(r):
        data = [[j, k, i] for i, j, k in data]
    data = [[f[0]*j[0], f[1]*j[1], f[2]*j[2]] for j in data]
    return data

def checkDirections(a, b):
    b = b.copy() #modify b orientation
    flips = [[1,1,1],[1,1,-1],[1,-1,1],[-1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1],[-1,-1,-1]]
    for z in range(3):
        for i in flips:
            bc = rotateflip(b, z, i) #data, rotations, coord flips
            bloc = checkScanners(a, bc)
            if bloc: return bloc, z, i 
            #else: print(z, i, 'failed')

def connectScanners(data):
    notcollected = list(range(len(data)))
    # order = [6, 10, 23] #then bricks
    # for i in order: notcollected.remove(i)
    # notcollected = order + notcollected

    collectivedata = data[0]
    notcollected.remove(0)

    #print(notcollected)
    while len(notcollected) > 0:
        for i in notcollected:
            print(i)
            # print('\n', collectivedata)
            bdata = checkDirections(collectivedata, data[i])
            if not bdata: continue
            bloc, brotates, bflips = bdata
            print(i, bloc)
            b = rotateflip(data[i], brotates, bflips)
            b = [[bloc[i]-j[i] for i in range(3)] for j in b]

            for j in b:
                if j not in collectivedata: collectivedata.append(j)
            notcollected.remove(i) #does stuff in wonky order
    print(collectivedata, len(collectivedata))
    

connectScanners(data)


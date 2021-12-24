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
            bloc = [a1[0]-b1[0], a1[1]-b1[1], a1[2]-b1[2]]
            countAligned = 0
            for a2 in ac:
                for b2 in bc:
                    if [a2[0]-b2[0], a2[1]-b2[1], a2[2]-b2[2]] == bloc:
                        countAligned+=1
                        # print(a1, b1, a2, b2, countAligned, bloc)
                        bc.remove(b2)
                        break
                if countAligned >= 11: return bloc

def rotateflip(data, axis, up):
    data = [i.copy() for i in data]
    match axis:
        case 0: pass
        case 1: #face -x
            data = [[-x, -y, z] for x, y, z in data]
        case 2: #face y
            data = [[y, -x, z] for x, y, z in data]
        case 3: #face -y
            data = [[-y, x, z] for x, y, z in data]
        case 4: #face z
            data = [[z, y, -x] for x, y, z in data]
        case 5: #face -z
            data = [[-z, y, x] for x, y, z in data]
    for i in range(up):
        data = [[x, z, -y] for x, y, z in data]
    return data

def checkDirections(a, b):
    for axis in range(6): #facing:
        for up in range(4):
            bc = rotateflip(b, axis, up)
            if bloc := checkScanners(a, bc): return bloc, axis, up

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
            if bdata:=checkDirections(collectivedata, data[i]):
                bloc, baxis, bup = bdata
                print(i, bloc)
                b = rotateflip(data[i], baxis, bup)
                b = [[bloc[i]+j[i] for i in range(3)] for j in b]
                #for z in b: print(z)
                for j in b:
                    if j not in collectivedata: collectivedata.append(j)
                notcollected.remove(i) #does stuff in wonky order
    print(collectivedata, len(collectivedata))

connectScanners(data)

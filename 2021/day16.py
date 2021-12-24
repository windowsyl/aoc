#data = open('day16inputexample.txt', 'r').readlines()[:-1]
decode = open('day16decode.txt', 'r').readlines()
decode = {i.split()[0]:i.split()[2] for i in decode}

data = open('day16input.txt','r').read()
#data = '9C0141080250320F1802104A08'
data = ''.join([decode[i] for i in data])

def findChildren(data):
    if data[0] == '0':
        lenB = int(data[1:16], 2)
        buffer, data = data[16:16+lenB], data[16+lenB:]
        vals = []
        while buffer:
            a, buffer = parsePacket(buffer)
            vals.append(a)
        return vals, data
    else:
        lenP = int(data[1:12], 2)
        data = data[12:]
        vals = []
        for i in range(lenP):
            a, data = parsePacket(data)
            vals.append(a)
        return vals, data

def prod(vals):
    prod = vals[0]
    for i in vals[1:]: prod *= i
    return prod

def checkInt(vals, func):
    if type(vals) is int: return vals
    return func(vals)

def parsePacket(data):
    V, ID, data = int(data[0:3], 2), int(data[3:6], 2), data[6:]
    if ID == 4:
        num = ''
        while data[0] == '1': #'0' isn't falsey :(
            num += data[1:5]
            data = data[5:]
        num += data[1:5]
        return int(num, 2), data[5:]
    vals, data = findChildren(data)
    if ID == 0: return checkInt(vals, sum), data
    if ID == 1: return checkInt(vals, prod), data
    if ID == 2: return checkInt(vals, min), data
    if ID == 3: return checkInt(vals, max), data
    if ID == 5: return int(vals[0] > vals[1]), data
    if ID == 6: return int(vals[0] < vals[1]), data
    if ID == 7: return int(vals[0] == vals[1]), data

print(parsePacket(data))

        

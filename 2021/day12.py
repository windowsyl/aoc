data = open('day12input.txt','r').read().split('\n')[:-1]
data = [i.split('-') for i in data]

tunnels = {}
for i in data:
    if i[0] in tunnels:
        tunnels[i[0]].append(i[1])
    else:
        tunnels[i[0]] = [i[1]]

    if i[1] in tunnels:
        tunnels[i[1]].append(i[0])
    else:
        tunnels[i[1]] = [i[0]]

def nextStep(key, small):
    if key == 'end': return 1
    new = small[:]
    if key[0] in 'qwertyuiopasdfghjklzxcvbnm':
        if key in small: return 0
        new += [key]
    return sum([nextStep(i, new) for i in tunnels[key]])

print('p1:', nextStep('start', []))

def nextStepP2(key, small, second):
    if key == 'end': return 1
    new = small[:]
    if key[0] in 'qwertyuiopasdfghjklzxcvbnm':
        if key in small:
            if second or key == 'start': return 0
            second = True
        new += [key]
    return sum([nextStepP2(i, new, second) for i in tunnels[key]])

print('p2:', nextStepP2('start', [], False))
data = open('day3input.txt','r').read()
locS = [0, 0]
dict = {str(locS): 1}

for i in data:
    if i == '^': locS[0] += 1
    elif i == 'v': locS[0] -= 1
    elif i == '>': locS[1] += 1
    elif i == '<': locS[1] -= 1
    else: print('aaaaaaa')
    if str(locS) in dict: dict[str(locS)] += 1
    else: dict[str(locS)] = 1
print('day 1:', len(dict))

Smoves = True
locS = [0, 0]
locR = [0, 0]
dict = {str(locS) : 1}

for i in data:
    p = [locR, locS][Smoves]
    if i == '^': p[0] += 1
    elif i == 'v': p[0] -= 1
    elif i == '>': p[1] += 1
    elif i == '<': p[1] -= 1
    else: print('aaaaaaa')
    if str(p) in dict: dict[str(p)] += 1
    else: dict[str(p)] = 1
    Smoves = not Smoves
print('day 2:', len(dict))


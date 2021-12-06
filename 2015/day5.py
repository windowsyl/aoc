data = open('day5input.txt','r').read().split('\n')[:-1]
count = 0
for i in data:
    if not any(['ab' in i, 'cd' in i, 'pq' in i, 'xy' in i]):
        vCount = 0
        hasPair = False
        lastLetter = False
        for j in i:
            if j in 'aeiou': vCount += 1
            if lastLetter == j: hasPair = True
            else: lastLetter = j
        if hasPair and vCount > 2: count += 1
print('day 1:', count)

count = 0
#for i in data:
for i in data:
    l1 = False
    l2 = False
    hasSandwhich = False
    for j in i:
        if j == l1 or hasSandwhich: hasSandwhich = True
        else: l1, l2 = l2, j
    if hasSandwhich:
        for j in range(len(i)-1):
            if len(i.split(i[j:j+2])) > 2:
                count+=1
                #print(i, i[j:j+2], l1)
                break

print('p2 :', count)
data = open('day10input.txt', 'r').read().split('\n')[:-1]

stack = []
swap = {'<':'>', '(':')', '{':'}', '[':']'}
sum = 0
scores = {')':3, ']':57, '}':1197, '>':25137}
for i in data:
    breakout = False
    for j in i:
        if j in swap: stack.append(j)
        else:
            for k in swap:
                if j == swap[k]:
                    if k == stack[-1]: stack.pop()
                    else:
                        sum += scores[j]
                        breakout = True
                        break
            if breakout: break
    stack = []
print(sum)
data = open('day10inputexample.txt', 'r').read().split('\n')

scores = {')':1, ']':2, '}':3, '>':4}


sum = []
stack = []
for i in data:
    lineScore = 0
    breakout = False
    stack = []
    for j in i:
        if j in swap: stack.append(j)
        else:
            for v in swap.values():
                if j == v:
                    if k == stack[-1]: stack.pop()
                    else:
                        print(i, 'corrupted')
                        breakout = True
                        break
            if breakout: break
    if breakout: continue
    print(i, ''.join(stack))
    stack = [swap[i] for i in stack]
    print(i, ''.join(stack))
    while len(stack) != 0:
        lineScore *= 5
        lineScore += scores[stack.pop()]
    sum.append(lineScore)
print(sum)
#print(sorted(sum)[int(len(sum)/2+0.5)])
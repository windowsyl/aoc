data = list(open('day12input.txt', 'r').read())
nums = '-0123456789'
sum = 0

def counter(x):
    if len(x) == 0: return 0
    innersum = 0
    while True:
        if x[0] not in nums:
            x.pop(0)
            if len(x) == 0: break
            else: continue
        number = [x[0]]
        i = 1
        while True:
            if x[i] in nums:
                number.append(x[i])
                i += 1
            else: break
        x = x[i+1:]
        innersum += int(''.join(number))
    return innersum

def omgParsing(x):
    chunk = [x.pop(0)]
    while x[0] != '}':
        if x[0] == '{': chunk.extend(omgParsing(x))
        else: chunk.append(x.pop(0))
    else: chunk.append(x.pop(0))   
    if ':"red"' in ''.join(chunk): 
        return []  
    return chunk

chunk = []
while True:
    if len(data) == 0: break
    if data[0] == '{':
        sum += counter(chunk)
        chunk = omgParsing(data)
        sum += counter(chunk)
        chunk = []
    else: chunk.append(data.pop(0))

print(sum)
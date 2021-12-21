data = open('day14input.txt', 'r').read().split('\n')

polymer, rules = data[0], data[2:-1]
rules = {i.split(' ')[0]:i.split(' ')[2] for i in rules}
finalcount = {i:0 for i in rules.values()}
rules = {i:[i[0]+rules[i], rules[i]+i[1]] for i in rules}

def occurrences(string, sub): #ripped from stack overflow
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

count = {i:occurrences(polymer, i) for i in rules}

for a in range(40):
    ncount = {i:0 for i in count}
    for i in count:
        ncount[rules[i][0]] += count[i]
        ncount[rules[i][1]] += count[i]
    count = ncount

print(count) 
for i in count:
    finalcount[i[0]] += count[i]
finalcount[polymer[-1]] += 1
print(max(finalcount.values())-min(finalcount.values()))
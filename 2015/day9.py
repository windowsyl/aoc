data = open('day9input.txt', 'r').read().split('\n')[:-1]
data = [i.split() for i in data]
locations = []
[locations.append(i[0]) for i in data if i[0] not in locations]
locations.append(data[len(data)-1][2])

dists = {}
for i in data:
    dists[i[0]+i[2]] = int(i[4])
    dists[i[2]+i[0]] = int(i[4])
#print(dists)
def distance(current, dests):
    #print(current, dests)
    if len(dests) == 1:
        return dists[current+dests[0]]
    x = [dists[current+dest]+distance(dest, [x for x in dests if x != dest]) for dest in dests]
    return max(x)   

x = [distance(i, [x for x in locations if x != i]) for i in locations]
print(max(x))
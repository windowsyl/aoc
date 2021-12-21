data = open('day14input.txt', 'r').read().split('\n')[:-1]
#data = "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\nDancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.".split('\n')
data = [i.split(' ') for i in data]

#for i in data: print(i)

dists = []
for i in data:
    dist = 0
    rest = 0
    run = 0
    for j in range(2503):
        if run < int(i[6]):
            rest = 0
            run += 1
            dist += int(i[3])
        elif rest < int(i[-2]):
            rest += 1
        else:
            run = 0

    dists.append(dist)

print(max(dists))

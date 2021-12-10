data = open('day13inputexample.txt','r').read().split('\n')
data = open('day13input.txt', 'r').read().split('\n')[:-1]

data = [i.split(' ') for i in data]
data = [[''.join([k if k != '.' else '' for k in j]) for j in i] for i in data] #drop the periods

people = []
[people.append(i[0]) for i in data if i[0] not in people]

friendships = {}
for i in data:
    if i[2] == 'gain': friendships[i[0]+i[-1]] = int(i[3])
    else: friendships[i[0]+i[-1]] = -int(i[3])
for person in people:
    friendships[person+'You'] = 0
    friendships['You'+person] = 0
people.append('You')

def happiness(seating):
    sum = 0
    for i in range(len(seating)):
        #print(i, seating[i], seating[(i+1)%len(seating)], friendships[seating[i]+seating[(i+1)%len(seating)]], friendships[seating[(i+1)%len(seating)]+seating[i]]) 
        sum += friendships[seating[i]+seating[(i+1)%len(seating)]]
        sum += friendships[seating[(i+1)%len(seating)]+seating[i]]
    return sum

from itertools import permutations
seatings = permutations(people)

print(max([happiness(i) for i in seatings]))

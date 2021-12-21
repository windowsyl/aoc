data = open('day14inputexample.txt', 'r').read().split('\n')

polymer, rules = data[0], data[2:-1]
rules = {i.split(' ')[0]:i.split(' ')[2] for i in rules}
for i in range(10):
    np = []
    for j in range(len(polymer)-1):
        np.append(polymer[j])
        if polymer[j]+polymer[j+1] in rules:
            np.append(rules[polymer[j]+polymer[j+1]])
    np.append(polymer[-1])
    polymer = np

counts = [polymer.count(i) for i in 'QWERTYUIOPASDFGHJKLZXCVBNM' if polymer.count(i)]
print(max(counts)-min(counts))
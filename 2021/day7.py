data = open('day7input.txt', 'r').read().split(',')
data = [int(i) for i in data]
#data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
x = []
for j in range( max(data)):
    sum = 0
    for i in data:
        sum += abs(i-j)*(abs(i-j)+1)/2
    print(j, sum)
    x.append(sum)
print(min(x), x.index(min(x)), len(x))
x = open('day2input.txt', 'r').read().split('\n')[:-1]
#print(x)
x = [i.split('x') for i in x]
x = [[int(j) for j in i] for i in x]
x = [sorted(i) for i in x]
day1 = 0
day2 = 0

for i in x:
    day1 += (i[0]+i[1])*2*i[2]+3*(i[0]*i[1])
    day2 += 2*(i[0]+i[1])+i[0]*i[1]*i[2]
print('day 1:', day1)
print('day 2:', day2)
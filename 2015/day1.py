x = open('day1input.txt','r').read()
floor = 0
goneToB = False
for i in range(len(x)):
    if x[i] == '(': floor+=1
    elif x[i] == ')':
        floor-=1
        if (floor < 0) and not goneToB:
            print('day 2:', i+1)
            goneToB = True
    else: print('aaaaaaa')
print('day 1:', floor)
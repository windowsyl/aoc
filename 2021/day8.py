x = open('day8input.txt', 'r').read().split('\n')[:-1]
x = [i.replace(' | ', ' ').split(' ') for i in x]

#x = open('day8inputexample.txt', 'r').read().split('\n')[:-1]
#x = [i.replace(' | ', ' ').split(' ') for i in x]

sum = 0
for i in x:
    #oldsum=sum 
    decode = {}
    for j in range(10): #1, 4, 7, 8
        if len(i[j]) in [2, 3, 4, 7]:
            decode[{2:1, 3:7, 4:4, 7:8}[len(i[j])]] = i[j]
    for j in range(10): #2, 3, 5
        if len(i[j]) == 5:
            if all(k in i[j] for k in decode[7]):
                decode[3] = i[j]
            elif all(k in i[j] for k in decode[4].replace(decode[1][0], '').replace(decode[1][1], '')):
                decode[5] = i[j]
            else:
                decode[2] = i[j]
        elif len(i[j]) == 6:
            if all(k in i[j] for k in decode[1]):
                if all(k in i[j] for k in decode[4]):
                    decode[9] = i[j]
                else:
                    decode[0] = i[j]
            else:
                decode[6] = i[j]
    flipped = {''.join(sorted(v)): k for k, v in decode.items()}
    for j in range(10, 14):
        for key in flipped:
            if ''.join(sorted(i[j])) == key:
                sum+=10**(13-j)*flipped[key]
                #break #for speed, these should be elifs
    #print(sum-oldsum)
print(sum)
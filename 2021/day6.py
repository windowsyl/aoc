data = open('day6input.txt', 'r').read().split(',')
data[-1] = data[-1].replace('\n','')
data = [int(i) for i in data]

#data=[3,4,3,1,2] #example

for i in range(80):
    #print(i)
    for fish in range(len(data)):
        if data[fish] == 0:
            data[fish] = 6
            data.append(8)
        else:
            data[fish] -= 1
print('p1:', len(data))


data = open('day6input.txt', 'r').read().split(',')
data[-1] = data[-1].replace('\n','')
data = [int(i) for i in data]

#data=[3,4,3,1,2] #example

dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in data:
    dict[i] += 1

for i in range(256):
    for key in dict:
        if key == 0:
            dict[7]+=dict[0] #both are gonna be counted again this day
            dict[9]+=dict[0]
            dict[0]=0
        else:
            dict[key-1] = dict[key]
    dict[9]=0
    #print([dict[key] for key in dict])

sum = 0
for key in dict:
    sum += dict[key]
print('p2:', sum)
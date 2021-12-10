data = open('day8input.txt', 'r').read()
#data = "\"\"\n\"abc\"\n\"aaa\\\"aaa\"\n\"\\x27\"\n"
data=data.split('\n')[:-1]
print(data)

sum=0
for string in data:
    old = sum
    oldstring = string
    sum += len(string.split('\\\\'))-1
    string = string.replace('\\\\', '')
    sum += len(string.split("\\\""))-1
    sum += 3*(len(string.split('\\x'))-1)
    sum+=2
    print(oldstring, sum-old)
print('p1:', sum)
#1152 too low
#1349 too high
sum = 0
for string in data:
    sum += 2
    sum += len(string.split('\\'))-1
    sum += len(string.split('\"'))-1
print('p2:', sum)
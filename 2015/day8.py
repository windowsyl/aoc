data = open('day8input.txt', 'r').read()
#data = "\"\"\n\"abc\"\n\"aaa\\\"aaa\"\n\"\\x27\"\n"
print(len(data))
data=data.split('\n')[:-1]
print(data)

print(len(data)+598+127*2)
sum=0
for string in data:
    old = sum
    sum += len(string.split("\\\""))-1
    sum += len(string.split('\\\\'))-1
    sum += 3*(len(string.split('\\x'))-1)
    sum -= 3*(len(string.split('\\\\x'))-1)
    sum += 3*(len(string.split('\\\\\\x'))-1)
    sum+=2
    print(string, sum-old)
print(sum)
#1152 too low
#1349 too high

data = open('day8input.txt', 'r').read().replace('\n','')
print(len(data))
print(len(data).replace("\\\\", "\\").replace("\\\"").replace())
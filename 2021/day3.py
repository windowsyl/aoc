x = open('inputday3.txt','r').read().split('\n')[:-1]
gamma = 0
for i in range(12):
	count = 0
	for j in x:
		count += int(j[i])
	print(count, len(x)/2)
	if count>(len(x)/2):
		gamma += 10 ** (11-i)
print(gamma)
print(int(str(gamma),2))
e = int(str(gamma),2) ^ (2**12-1)
print(bin(e)[2:])
print(e)
print(e*int(str(gamma),2))

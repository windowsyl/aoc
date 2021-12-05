with open('inputday1.txt', 'r') as f:
	x = f.read().split('\n')
sum = 0
y = [int(y) for y in x[:-1]]

for i in range(1, len(y)):
	if y[i] > y[i-1]:
		sum += 1
print(sum)
sum = 0
for i in range(3, len(y)):
	if y[i] > y[i-3]:
		sum += 1
print(sum)	

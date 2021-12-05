x = open('inputday4.txt', 'r').read().split('\n\n')

y, x = x[0].split(','), x[1:]
print(y)

x = [i.replace('\n', ' ').replace('  ', ' ') for i in x]
x = [i.split(' ') for i in x]
x = [[j for j in i if j != ''] for i in x]


def hasBingo(arr):
	for i in range(5):
		z = []
		for j in range(5):	
			if type(arr[i*5+j]) is not int: break
			z.append(arr[i*5+j])
			if j == 4:
				print('bing row', z)
				return True
	for i in range(5):
		z = []
		for j in range(5):	
			if type(arr[i+j*5]) is not int: break
			z.append(arr[i+j*5])
			if j == 4:
				print('bingo col', z)
				return True
	return False
def getScore(arr):
	unmarked = 0
	for i in arr:
		if type(i) is not int: unmarked += int(i)
	return unmarked

for pull in y:
	for board in range(len(x)):
		for k in range(len(x[board])):
			if x[board][k] == pull: x[board][k] = int(pull)
		if hasBingo(x[board]):
			print(int(pull)*getScore(x[board]))
			x[board] = ['r' for z in x[board]]

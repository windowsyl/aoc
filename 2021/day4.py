x = open('inputday4.txt', 'r').read().split('\n\n')
y, x = x[0].split(','), x[1:]

x = [i.replace('\n', ' ').replace('  ', ' ') for i in x]
x = [i.split(' ') for i in x]
x = [[j for j in i if j != ''] for i in x]

def hasBingo(arr):
	for i in range(5):
		for j in range(5):
			if arr[i*5+j] != 1: break
			if j == 4: return True
	for i in range(5):
		for j in range(5):
			if arr[i+j*5] != 1: break
			if j == 4: return False
	return False
def getScore(arr):
	unmarked = 0
	for i in arr:
		if i != 1:
			unmarked += int(i)
	return unmarked

for i in y:
	for j in x:
		for k in range(len(j)):
			if j[k] == i: j[k] = 1
		if hasBingo(j):
			print(int(i)*getScore(j))
			exit()

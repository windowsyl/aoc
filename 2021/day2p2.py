x = open('inputday2.txt', 'r').read().split('\n')[:-1]
h = 0
d = 0
aim = 0
for i in x:
	if i[0] == 'f':
		h += int(i[-1])
		d += aim * int(i[-1])
	elif i[0] == 'd':
		aim += int(i[-1])
	else:
		aim -= int(i[-1])
print(h*d)

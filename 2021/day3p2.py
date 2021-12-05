x = open('inputday3.txt','r').read().split('\n')[:-1]
y = x
a = b = 0
for i in range(11):
	count = 0
	for j in y:
		count += int(j[i])
	bit = count>=len(y)/2
	y = [j for j in y if int(j[i])==bit]
	if len(y)==1: a=y[0]
y = x
for i in range(11):
	count = 0
	for j in y:
		count += int(j[i])
	bit = count<len(y)/2
	y = [j for j in y if int(j[i])==bit]                                                                         
	if len(y)==1: b=y[0]
print(int(str(a,2)*int(str(b),2))

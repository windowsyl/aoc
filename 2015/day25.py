def valFromCol(col):
    return int(col*(col-1)/2+1)
def nextVal(val):
    return (val*252533)%33554393
row = 2947
col = 3029

x = 20151125
num = valFromCol(row+col-1)+col-1
print(num)
for i in range(num-1):
    x = nextVal(x)
print(x)
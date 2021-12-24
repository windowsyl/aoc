from math import sqrt

xb = (253, 280)
yb = (-73, -46)

xv, yv = 23, 4
def testTragectory(xv, yv):
    maxy = yv*(yv+1)/2
    fallestimate = round((-1+sqrt(8*(maxy-yb[0])+1))/2+0.5)
    fallestimate-=1
    for falltime in range(fallestimate-2, fallestimate+1): #arghh rounding properly is hard this is easier
        totaltime = yv + falltime + 1
        if xv>totaltime: x = xv*(xv+1)/2-(xv-totaltime)*(xv-totaltime+1)/2
        else: x = xv*(xv+1)/2
        y = maxy - falltime*(falltime+1)/2
        if all([x>=xb[0], x<=xb[1], y>=yb[0], y<=yb[1]]):
            return True
    return False

print([testTragectory(xv, yv) for xv in range(300) for yv in range(-100,100)].count(True))
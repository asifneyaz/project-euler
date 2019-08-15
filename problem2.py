import math
def isFibonnaci(n):
    return isPerfectsquare(5*(n*n)+4) or isPerfectsquare(5*(n*n)-4)

def isPerfectsquare(x):
    s = int(math.sqrt(x))
    return s*s == x

sumoffib = 0
for i in range(1,4000001):
    if isFibonnaci(i) is True:
        if i%2 == 0:
            sumoffib = sumoffib + i

print(sumoffib)


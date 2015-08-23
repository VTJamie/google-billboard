import math
from decimal import *
getcontext().prec = 12

def isPrime(val):
    if val % 2 == 0:
        return False
    else:
        maxval=math.ceil(math.sqrt(val))
        for x in range(3, maxval+1):
            if val % x == 0:
                return False
        return True


numzeros=9


multval=int(math.pow(10, numzeros))

firstprime=0
fifth49=0
found=0
x = 0
while firstprime==0 or found<5:
    numzeros += 1
    multval=int(math.pow(10, numzeros))
    getcontext().prec += 1
    numtuple=Decimal(1).exp().as_tuple()[1][x:10+x]
    val=int(''.join(map(str, numtuple)))

    if isPrime(val):
        firstprime=val
    if sum(numtuple) == 49:
        found += 1
        fifth49=val
    x += 1

print('First Prime: %d' % firstprime)

#I thought that it was an exponentially increasing function on the start position of the number
# , looked up the answer and found I was thinking too complicated
print('Fifth 49: %d' % fifth49)

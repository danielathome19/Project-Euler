import math, itertools

def cf_period(r):
    p = int(math.sqrt(r))   # floor of sqrt(r)
    if p*p == r: return 0   # Square number
    q=1
    remainders = {}

    for pos in itertools.count(1):
        q=(r-(p*p))/q
        floor=int((math.sqrt(r)+p) /float(q))
        p = -1* (p- (floor*q))
        if (p,q) in remainders:
            return pos-remainders[p,q]
        remainders[p,q] = pos

print len([x for x in range(2,10001) if cf_period(x)%2==1])
raw_input('Press Enter to exit')
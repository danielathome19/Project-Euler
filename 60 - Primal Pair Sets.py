primelist = [2, 3, 5]

def IsPrime(n):
    if n==1: return False
    for p in primelist:
        if p*p > n: break
        if n % p == 0: return False
    return True

def MakePrime(upto):
    n = 6*(primelist[-1]/6 + 1)
    while n < upto:
        if IsPrime(n+1): primelist.append(n+1)
        if IsPrime(n+5): primelist.append(n+5)
        n += 6
        
MakePrime(10000)

def Combine(p, q):
    order = 10
    while order <= q: order *= 10
    return p*order+q

print len(primelist), 'primes.'

primepairs = {}
            
for i, p in enumerate(primelist):
    for q in primelist[i+1:]:
        if IsPrime(Combine(p,q)) and IsPrime(Combine(q,p)):
            if p in primepairs:
                primepairs[p].append(q)
            else:
                primepairs[p] = [q]

print sum([len(v) for k,v in primepairs.iteritems()]), 'pairs.'

primetrips = {}

for p,qs in primepairs.iteritems():
    if len(qs) < 4: continue
    for i,q in enumerate(qs):
        for r in qs[i+1:]:
            if q in primepairs and r in primepairs[q]:
                if (p,q) in primetrips:
                    primetrips[(p,q)].append(r)
                else:
                    primetrips[(p,q)] = [r]

print sum([len(v) for k,v in primetrips.iteritems()]), 'triples.'

primequads = {}

for ps,qs in primetrips.iteritems():
    if len(qs) < 3: continue
    for i,q in enumerate(qs):
        for r in qs[i+1:]:
            if q in primepairs and r in primepairs[q]:
                tup = ps+(q,)
                if tup in primequads:
                    primequads[tup].append(r)
                else:
                    primequads[tup] = [r]

print sum([len(v) for k,v in primequads.iteritems()]), 'quads.'

primequints = {}

for ps,qs in primequads.iteritems():
    if len(qs) < 2: continue
    for i,q in enumerate(qs):
        for r in qs[i+1:]:
            if q in primepairs and r in primepairs[q]:
                tup = ps+(q,)
                if tup in primequints:
                    primequints[tup].append(r)
                else:
                    primequints[tup] = [r]

print primequints
for ps,qs in primequints.iteritems():
    print sum(ps)+sum(qs)

raw_input('Press Enter to exit')
maxsshape, digits = 8, 2

P, Pvals, solutions = lambda s, n: n * ((s - 2) * n + 4 - s) / 2, {}, []
for s in range(3, maxsshape + 1):
    Pvals[s], n, v = {}, 0, 0
    while v < 10 ** (2 * digits):
        n += 1
        v = P(s, n)
        if 10 ** (2 * digits - 1) <= v < 10 ** (2 * digits):
            d1, d2 = divmod(v, 10 ** digits)
            if d2 / 10 == 0: continue
            if not Pvals[s].has_key(d1): Pvals[s][d1] = []
            Pvals[s][d1].append(d2)

search = [{'left': set(range(4, maxsshape + 1)), 'found': [(3, k)]} for k in Pvals[3].keys()]
while len(search) > 0:
    current = search.pop()
    left, found = current['left'], current['found']
    lastd = found[-1]   #syntax: (shape, 2digit prefix)
    nextdigs = Pvals[lastd[0]].get(lastd[1], [])
    if len(left) == 0:
        if found[0][1] in nextdigs:
            solutions.append(found)
        continue

    for nextd in reduce(lambda a, b: a + b, ([(s, d) for d in nextdigs] for s in left)):
        search.append({'left': left - set([nextd[0]]), 'found': found + [nextd]})

for solution in solutions:
    print solution, " Total:", (1 + 10 ** digits) * sum(d[1] for d in solution)

raw_input('Press Enter to exit')
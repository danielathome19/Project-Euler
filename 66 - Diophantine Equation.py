maxd = 1000

def contfr(n):
	x, y = 1, int(n ** 0.5)
	q, lastq = 1, 2 * y
	while q != lastq:
		q = int(x * (n ** 0.5 + y) / (n - y ** 2))
		yield q
		x, y = (n - y ** 2) // x, q * (n - y ** 2) // x - y

dees = [i for i in xrange(2, maxd + 1) if int(i ** 0.5 + 0.5) ** 2 != i]
deesforxsolns = {}

for d in dees:
	seqvals = [val for val in contfr(d)]
	seqvals.insert(0, int(d ** 0.5))

	if (len(seqvals) - 2) & 1:
		seqvals.pop(-1)
	else:
		seqvals.extend(seqvals[1:-1])

	den, num = 1, seqvals[-1]
	for i in xrange(len(seqvals) - 2, -1, -1):
		num, den = seqvals[i] * num + den, num # GCD always 1
	deesforxsolns[num] = d # num = x, den = y

print deesforxsolns[max(deesforxsolns.iterkeys())]
raw_input('Press Enter to exit')
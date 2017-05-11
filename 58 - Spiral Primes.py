from mctools import isprime 
PRIME_PERCENT = 10
n = 3; prime_count = 0 
while True:
    for i in (1, 2, 3):
        prime_count += isprime( n*n - i*(n-1))
    ratio = (100 * prime_count) / (2*n - 1)
    if ratio < PRIME_PERCENT: break
    n += 2
print n # 26241 765 ms
raw_input('Press Enter to exit')
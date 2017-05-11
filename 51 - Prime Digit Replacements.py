import time,math

def find_prime_family():
    
    primes = find_primes(1e6,[])
    
    prime_dict = {}
    primes_short = []
    for prime in primes[:]:
        if prime > 56000:
            prime_dict[prime] = 1
            primes_short.append(prime)
    
    test_nums = [str(i) for i in range(0,10) ]
    match_dict = {}
    match_found = False
    for prime in primes_short[:]:
        match_dict[prime] = []
        prime_str = str(prime)
        prime_stub = prime_str[:-1]
        last_digit = prime_str[-1]
        
        prime_stub_list = list(prime_stub)
        prime_stub_list.sort()
        unique_list = list(set(prime_stub_list))

        for num in unique_list[:]:
            for i in test_nums:
                temp_stub = prime_stub
                temp_stub = temp_stub.replace(num,str(i))
                temp_num = int(temp_stub + last_digit)
                if prime_dict.has_key(temp_num):
                    match_dict[prime].append(temp_num)
            if len(match_dict[prime][:]) == 8:
                match_found = True
                break
            else:
                match_dict[prime] = []
        if match_found == True:
            print prime
            print match_dict[prime]
            match_found = False

def find_primes(max_num,prime_divisors):
    if len(prime_divisors) < 2:
        prime_divisors = [2,3]
    num = prime_divisors[-1] + 2
    while num < max_num:
        if is_prime(num,prime_divisors):
            prime_divisors.append(num)
        num += 2
    return prime_divisors

def is_prime(num,prime_divisors):
    max_divisor = int(math.sqrt(num)) + 1

    if num == 1:
        return False
    elif num in [2,3,5,7]:
        return True
    for divisor in prime_divisors:
        if num % divisor == 0:
            return False
        if divisor > max_divisor:
            break
    return True


start_time = time.time()

find_prime_family()

exec_time = time.time() - start_time
print 'Total Execution Time: ' + exec_time.__str__() + '(s)'
raw_input('Press Enter to exit')
Limit=1000000   
factors=[0]*Limit
count=0
for i in xrange(2,Limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print i-3 
            break
    else:
        count = 0

raw_input('Press Enter to exit')
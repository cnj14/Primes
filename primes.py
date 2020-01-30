def Main():
    list = []
    primes = []
    composites = []
    low = int(input("Minimum number in your range: "))
    counter = low
    high = int(input("Maximum number in your range: "))
    while counter <= high:
        list.append(counter)
        counter +=1
    for n in list:
        k = 2
        factors = []
        while k <= n:
            if n%k==0:
                factors.append(k)
                k+=1
            else:
                k +=1
        if len(factors) == 1:
            primes.append(n)
        else:
            composites.append(n)
    print("The prime numbers between", low, "and", high, "are: ",primes)
    
    
            

Main()
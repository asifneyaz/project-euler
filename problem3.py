def primefactor(n):
    prime = True
    for i in range(2,n):
        if n%i == 0:
            prime = False
    return prime
            


def factor(n):
    largest_prime_factor = 1
    for i in range(2,n):
        if n%i == 0:
            if primefactor(i) is True:
                largest_prime_factor = i
    return largest_prime_factor

print(factor(13195))

        
    
        


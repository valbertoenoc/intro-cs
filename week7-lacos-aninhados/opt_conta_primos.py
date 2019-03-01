def e_primo(n):
    i = 2
    primo = True
    while i < n:
        if n % i == 0:
            primo = False
        
        i += 1 

    return primo


def n_primos(n):
    count = 0
    for i in range(2, n+1):
        if e_primo(i):
            count += 1
    
    return count

def primo(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1 

    return True

def maior_primo(n):
    i = n
    while i <= n:
        if primo(i):
            return i
        i -= 1

    return 2


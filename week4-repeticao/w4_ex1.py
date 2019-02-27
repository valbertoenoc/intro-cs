def fat(n):
    """
    factorial function
    """
    r = 1
    while n > 0:
        r *= n
        n -= 1

    return r


def fat_r(n):
    """
    factorial recursive function
    """
    if n == 0:
        return 1
    else: 
        return n * fat_r(n - 1) 


n = int(input())
print(fat(n))
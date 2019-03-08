def maiusculas(string):
    maiu_ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    maiusculas = ''
    for i in string:
        if i in maiu_ascii:
            maiusculas += i
    
    return maiusculas
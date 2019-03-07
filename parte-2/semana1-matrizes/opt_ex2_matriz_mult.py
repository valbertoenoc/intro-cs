def sao_multiplicaveis(m1, m2):
    d_m1 = (len(m1), len(m1[0]))
    d_m2 = (len(m2), len(m2[0]))

    if d_m1[1] == d_m2[0]:
        return True
    else:
        return False


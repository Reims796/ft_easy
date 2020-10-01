def ft_rev_num(a):
    if a > 0:
        a1 = a // 100 % 10
        a2 = a // 10 % 10
        a3 = a % 10
        itog = a3 * 100 + a2 * 10 + a1
    else:
        a = a * -1
        a1 = a // 100 % 10
        a2 = a // 10 % 10
        a3 = a % 10
        itog = (a3 * 100 + a2 * 10 + a1) * -1
    return itog


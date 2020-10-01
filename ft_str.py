def ft_str(a,b,c):
    s = (a + b + c)/2
    if a >= b + c or b >= a + c or c >= a + b:
        a = -1
        return a
    else:
        a = (s * (s - a)*(s - b)*(s - c)) ** 0.5
        return a

    


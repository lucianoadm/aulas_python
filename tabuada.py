def tabuada(x):
    n = 0
    r = 1
    while n <= 10:
        print(x, 'x', n, '=', r)
        n += 1
        r = x * n

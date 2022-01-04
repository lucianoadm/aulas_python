def potencia():
    n = int(input('Digite a base: '))
    k = int(input('Digite o expoente: '))

    pot = 1
    i = 0
    while i < k:
        pot = pot * n
        i += 1

    print(n, 'elevado a', k, '=', pot)

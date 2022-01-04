def maximo(a,b):
    max = 0
    if a > b:
        max = a
        return a
        print(a)
    else:
        max = b
        return b
        print(b)

a = int (input('escreva um numero: '))
b = int (input('escreva outro numero: '))
print(f'maximo({a}, {b})')
print(max)


def somador():
    n = int(input('Digite um numero inteiro, pressione (zero para terminar): \n'))
    soma = 0
    while n != 0:
        soma = soma + n
        n = int(input())
    print('soma total =', soma)

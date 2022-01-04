from math import factorial
def Fatorial (n , p):
   return factorial(n) / (factorial(p) * factorial(n-p))
n = 1
p = 1
while n != 0 or p != 0:
    try:
        n = int(input('Digite o numerador binominal: '))
        p = int(input('Digite o denominador binominal: '))
        print(Fatorial(n, p))
    except ValueError:
        if p > n:
            print('O denominador binominal não pode ser maior que o numerador binominal')
        else:
            print('Carácter inválido, tente novamente')
print('Fim do exercício')

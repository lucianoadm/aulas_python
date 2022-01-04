from math import sqrt
pergunta = 'S'
def Baskara(a,b,c):
    x1 = ((-b + sqrt(b ** 2 - ((4 * a) * c))) / 2 * a)
    x2 = ((-b - sqrt(b ** 2 - ((4 * a) * c))) / 2 * a)
    return x1, x2
while pergunta !='N':
    A = int(input('Digite un número inteiro: '))
    B = int(input('Digite un número inteiro: '))
    C = int(input('Digite un número inteiro: '))
    try:
        if A <= 0:
            print('Digite apenas números inteiros, positivos e maiores que 0')
            A = int(input('Digite un número inteiro: '))
        else:
            resultado = Baskara(A, B, C)
            print('O resultado desta equação do segundo grau é \n{}\n----------------------'.format(resultado))
            print('Para sair digite "N"\n--------------------------')
            pergunta = input('Deseja Continuar?[S/N]').strip().upper()
            if pergunta != 'N' and pergunta != 'S':
                print('Digite apenas "S" para continuar ou "N" para sair')
            elif pergunta == 'N':
                break
    except ValueError:
        print('Tente novamente')
print('==============\nFim do exercício\n==================')

import math
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = b**2-4*a*c
if delta == 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    print('A raiz dupla desta equação é:', r1)
else:
    if delta < 0:
        print('Esta equação não possui raízes reais.')
    else:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)
        if r1 < r2:
            print(f'As raízes da equação são: {r1} e {r2}')
        else:
            print(f'As raízes da equação são: {r2} e {r1}')

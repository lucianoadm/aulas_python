n = int(input('Digite um número: '))
primo = True
div = 2
while div < n and primo:
    if n % div == 0:
        primo = False
    div = div + 1
if primo and n != 1:
    print('primo')
else:
    print('não primo')

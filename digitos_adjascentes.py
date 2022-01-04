n = int(input('Digite um número: '))
igual = False
v_ant = n % 10
n = n // 10
v = 0
while n > 0 and not igual:
    v_atual = n % 10
    n = n // 10
    if v_atual == v_ant:
        igual = True
    v_ant = v_atual
if igual:
    print('sim')
else:
    print('não')

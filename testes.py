cont = 0
vista = 0
parcelado = 0
venda = 0
while cont < 2:
    vendedor = input("Digite o vendedor: ")
    valor = float(input('Digite o valor da venda: '))
    condicao = int(input('[] 1 - À vista - [] 2 - Parcelado'))
    cont += 1
    venda += valor
    if condicao == 1:
        vista = venda

    else:
        parcelado = venda - vista

print(f'Total à vista: {vista}')
print(f'Total parcelado: {parcelado}')


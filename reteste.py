produto = []
quantidade = []
valor_unit = []
estoque_min = []
reposicao = []
while True:
    produto.append(input('Digite o produto: '))
    estoque_min.append((int(input('Digite o estoque mínimo: '))))
    quantidade.append(int(input('Digite a quantidade do estoque: ')))
    valor_unit.append(float(input('Digite o valor unitári: ')))
    print('Digite A para adicionar\n'
          'digite s para sair: ')
    escolha = input('Digite: ').upper()
    if escolha == 'A':
        continue
    else:
        if escolha == 'S':
            print('Programa encerrado!')
            break
total_reposicao = 0
custo_reposicao = 0
busca = input('Digite o produto que deseja pesquisar: ')
for i in range(len(produto)):
    if busca == produto[i]:
        total_reposicao = estoque_min[i] - quantidade[i]
        custo_reposicao = valor_unit[i] * total_reposicao
        print(f'Produto: {produto[i]}')
        print(f'Estoque atual: {quantidade[i]}')
print(f'Total para reposição: {total_reposicao}')
print(f'Custo de reposição estimado {round(custo_reposicao,2)}')



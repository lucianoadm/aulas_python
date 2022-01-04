n=int(input('Digite a base: '))
k=int(input('Digite o expoente: '))
pot=1
i=0
while i<k:
    pot=pot*n
    i=i+1
print('A potência é',pot)
print('O valor de %d elevado a %d é %d' %(n,k,pot))

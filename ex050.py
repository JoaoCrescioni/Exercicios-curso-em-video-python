soma = 0
cont = 0
for c in range (0, 6):
    res = int(input('Digite um número: '))
    if res%2 == 0:
        soma += res
        cont +=1
print('A soma dos {} valores pares é {}'.format(cont, soma))

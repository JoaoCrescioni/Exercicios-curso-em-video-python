lista = []
while True:
    lista.append(int(input('Digite um número para adicionar a lista: ')))
    if lista[-1] in lista[:-1] and len(lista) > 1 :
        print('Valor já foi adicionado a lista! Digite outro!')
        del lista[-1]
    else:
        seguir = str(input('Deseja continuar? [S/N] : '))
        if seguir in 'Nn':
            break
print(lista)
print(f'Você digitou {len(lista)} elementos! ')
print(f'Os valores em ordem decrescente ficam {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O número 5 foi encontrado vez na lista!')
else:
    print('O número 5 não foi encontrado na lista!')

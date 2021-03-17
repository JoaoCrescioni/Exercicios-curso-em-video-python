lista_val = []
cont = 0
while True:
    cont+=1
    num = int(input(f'Digite o {cont}º valor: '))
    if num in lista_val:
        print('Valor já adicionado! Escolha outro!')
    else:
        #lista_val += [num]
        lista_val.append(num)
        print('Valor adicionado com sucesso! ')
    opcao = str(input('Deseja continuar? [S/N]')).upper()
    if opcao == 'N':
        break
print(f'Você digitou os valores {sorted(lista_val)}')

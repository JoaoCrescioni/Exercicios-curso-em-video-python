lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um número: '))
    if num%2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    opcao = str(input('Deseja continuar? [S/N] : '))
    if opcao in 'Nn':
        break
print(f'A lista de números digitados: {sorted(lista_par+lista_impar)}')
print(f'A lista de números pares digitados: {sorted(lista_par)}')
print(f'A lista de números impares digitados: {sorted(lista_impar)}')
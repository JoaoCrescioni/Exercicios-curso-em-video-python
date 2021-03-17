from random import randint
cont = 0
while True:
    comput = randint(0, 10)
    escolha_num = int(input('Escolha um número (0 a 10):'))
    soma = escolha_num+comput
    escolha_pi = ' '
    while escolha_pi not in 'PI':
        escolha_pi = str(input('Par ou Impar? (P ou I): ')).upper().strip()

    if soma%2 == 0 and escolha_pi == 'P':
        print(f'{comput} + {escolha_num} = {soma}')
        print('Você venceu!')
        cont += 1
    if soma%2 == 1 and escolha_pi == 'I':
        print(f'{comput} + {escolha_num} = {soma}')
        print('Você venceu!')
        cont += 1
    if soma%2 == 1 and escolha_pi != 'I':
        print(f'{comput} + {escolha_num} = {soma}')
        print('Você perdeu!')
        break
    if soma%2 == 0  and escolha_pi != 'P':
        print(f'{comput} + {escolha_num} = {soma}')
        print('Você perdeu!')
        break
if cont == 0:
    print('Você não ganhou nenhuma vez!')
elif cont == 1:
    print(f'Você ganhou uma vez!')
else:
    print(f'Você ganhou {cont} vezes seguidas!')
from random import randint
from time import sleep

escolha = str(input('Escolha Padra, Papel ou Tesoura! : ').strip().upper())
maquina = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
if maquina == 1 :
    print('O computador escolheu tesoura!')
    pc = 'TESOURA'
    if pc == escolha:
        print('Temos um empate!')
    elif pc != escolha and escolha=='PAPEL':
        print('O computador venceu!')
    else:
        print('Você venceu!')
elif maquina == 2:
    print('O computador escolheu pedra!')
    pc = 'PEDRA'
    if pc == escolha:
        print('Temos um empate!')
    elif pc != escolha and escolha=='TESOURA':
        print('O computador venceu!')
    else:
        print('Você venceu!')

elif maquina == 3:
    print('O computador escolheu papel!')
    pc = 'PAPEL'
    if pc == escolha:
        print('Temos um empate!')
    elif pc != escolha and escolha=='PEDRA':
        print('O computador venceu!')
    else:
        print('Você venceu!')




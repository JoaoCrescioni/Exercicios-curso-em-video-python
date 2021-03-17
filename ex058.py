from random import  randint
from time import sleep
num = 0
tentativas = 0
num2 = randint(0, 10)
while num2 != num:
    num = int(input('Adivinhe qual número o computador escolheu (0 a 10): ').strip())
    print('Processando...')
    sleep(3)
    tentativas += 1
    if num == num2 :
        print('Você acertou!')
    else:
        print('Você errou! Mais uma vez!')
        if num > num2:
            print('Um pouco menos...')
        else:
            print('Um pouco mais...')
if tentativas == 0:
    print('\n... e foi de primeira!')
elif tentativas == 1:
    print(' Foi necessária uma tentativa a mais para acertar!')
else:
    print(' Foram necessárias {} tentativas para acertar!'.format(tentativas))
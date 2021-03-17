import random
from time import sleep
num = int(input('Adivinhe qual número o computador escolheu (0 a 5): ').strip())
num2 = random.randint(0, 5)
print('Processando...')
sleep(3)
if num == num2 :
    print('Você acertou!')
else:
    print('Você errou!')
    print('Tente de novo! O número certo era {}'.format(num2))

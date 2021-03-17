from time import sleep as slp
from random import randint as rai
numPalp = int(input('Digite o número de jogos para serem sorteados: '))
jogos = []
for c in range (0,numPalp):
    while True:
        num = rai(1,61)
        if len(jogos) == 0:
            jogos.append(num)
        elif len(jogos) < 6:
            if num not in jogos:
                jogos.append(num)
        else:
            break
    slp(0.5)
    print(f'Aqui está o jogo {c+1}: {sorted(jogos)}')
    jogos.clear()
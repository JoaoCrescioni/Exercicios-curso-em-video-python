from random import randint as rai
from time import sleep as slp
cont = 1
dados = {'jogador1':rai(1,6), 'jogador2':rai(1,6),
         'jogador3':rai(1,6),'jogador4':rai(1,6)}
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    slp(1)
print('-='*25)
res = {key: val for key, val in sorted(dados.items(), key = lambda  ele: ele[1], reverse=True)}
for k,v in res.items():
    print(f'{cont}º lugar: {k} com {v}')
    cont+= 1

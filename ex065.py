maior = menor = c = 0
armazena = []
parada = ''
while parada != 'S':
    num = float(input('Digite os valores a serem conferidos: '))
    armazena += [num]
    c += 1
    if c >= 2:
        parada = str(input('Deseja parar? S ou N?').upper())
armazena.sort()
print(f'O maior número é {armazena[-1]} e o menor é {armazena[0]}')
print('A média entre os {} números é {} '.format(c, sum(armazena)/c))

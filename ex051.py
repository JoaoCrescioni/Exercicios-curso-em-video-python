primeiro = float(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
for c in range (1, 11):
    if c == 1 :
        print('O 1º termo é {}'.format(primeiro))
    else:
        primeiro += razao
        print('O {}º termo é {}'.format(c, primeiro))

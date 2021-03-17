primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
c= 1
while c < 11:
    print('O {:.0f}º termo é {} !'.format(c, primeiro))
    c+=1
    primeiro += razao

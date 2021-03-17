com1 = float(input('Digite o cm da primeira reta: '))
com2 = float(input('Digite o cm da segunda reta: '))
com3 = float(input('Digite o cm da terceira reta: '))
com4 = abs(com2-com3)
com5 = abs(com1-com3)
com6 = abs(com1-com2)
com7 = com2+com3
com8 = com1+com3
com9 = com1+com2

if com4<com1<com7 and com5<com2<com8 and com6<com3<com9:
    print('As retas formam um triângulo!!!', end='')
    if com1==com2==com3:
        print('...triângulo equilátero!', )
    elif com1==com2 or com1==com3 or com2==com3:
        print('...triângulo isósceles!')
    else:
        print('...triângulo escaleno!')


else:
    print('As retas não formam um triângulo!')

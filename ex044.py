preco = float(input('Digite o preço original do produto: '))
condicao = str(input('Escolha a opção de pagamento: À vista ou parcelado? ').strip().upper())

if preco == 0 :
    print('Mais informações são necessárias!')
else:
    if condicao == "A VISTA" or condicao == 'À VISTA':
        din_car = str(input('Você usará cartão ou dinheiro? : ').strip().upper())
        if din_car == 'DINHEIRO':
            print('O preço será de R$ {:.2f} !'.format(preco-preco/100*10))
        if din_car == 'CARTÃO':
            print('O preço será de R$ {:.2f} !'.format(preco-preco/100*10))
        else:
            print('Você escolheu uma opção inválida')
    elif condicao == 'PARCELADO':
        x2_x3 = int(input('Em quantas vezes você parcelará: 2 ou 3? '))
        if x2_x3 == 2:
            print('O preço será de R$ {:.2f} !'.format(preco))
        elif x2_x3 == 3:
            print('O preço final será de R$ {} !'.format(preco+preco/100*20))



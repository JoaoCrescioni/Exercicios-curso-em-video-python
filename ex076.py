listagem = ('Leite', '2.50',
            'Chocolate', '3.50',
            'Bolacha', '4.50',
            'Café', '6.50')
for c in range(0,len(listagem),2):
    print(f'{listagem[c]:.<30} R$ {listagem[c+1]}')

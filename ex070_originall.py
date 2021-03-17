total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1

    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA!'))

lista_nomes = lista_preco = []
mais_de_mil = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    lista_nomes += [nome]
    lista_preco += [preco]
    if preco > 1000:
        mais_de_mil +=1
    while preco <= 0:
        print('Digite um valor válido!')
        preco = float(input('Digite o preço do produto: '))
    cont = str(input('Quer continuar? [S/N]: ')).upper()
    while cont not in 'SsNn':
        print('Digite uma respostá válida!')
        cont = str(input('Quer continuar? [S/N]: '))
    if cont == 'N':
        break
junta_lista = zip(lista_preco, lista_nomes)
sorteia_lista = sorted(junta_lista)
juncao = zip(*sorteia_lista)
lista_preco, lista_nomes = [list(tuple) for tuple in juncao]
print(f'O total da compra foi R$ {sum(lista_preco)} ! ')
print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {lista_nomes[0]} que custa R${lista_preco[0]}!')
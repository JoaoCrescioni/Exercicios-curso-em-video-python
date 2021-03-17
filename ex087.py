matriz = list()
parSoma = []
terCol = []
lin2 = []
for c in range(0,9):
    if 0 <= c <= 2:
        matriz.append(int(input(f'Digite um valor para [0,{c}]: ')))
    elif 2 < c <=5:
        matriz.append(int(input(f'Digite um valor para [1,{c-3}]: ')))
    else:
        matriz.append(int(input(f'Digite um valor para [2,{c-6}]: ')))
print('=-'*20)
print(f'[ {matriz[0]} ][ {matriz[1]} ][ {matriz[2]} ] \n'
      f'[ {matriz[3]} ][ {matriz[4]} ][ {matriz[5]} ] \n'
      f'[ {matriz[6]} ][ {matriz[7]} ][ {matriz[8]} ]')
print('=-'*20)
for par in matriz:
    if par%2 == 0:
        parSoma.append(par)
print(f'A soma dos valores pares é igual a {sum(parSoma)}!')

for i,col3 in enumerate(matriz):
    if i == 2 or i == 5 or i ==8:
        terCol.append(col3)
print(f'A soma dos valores da terceira coluna é {sum(terCol)}!')

for i, maior in enumerate(matriz):
    if 3 <= i <=5:
        lin2.append(maior)
print(f'O maior valor da segunda linha é {max(lin2)}')
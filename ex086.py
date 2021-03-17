matriz = list()
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
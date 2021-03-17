lista = []
cont_maior = cont_menor = 0
for num in range (1,6):
    inp = int(input(f'Digite o {num}º valor: '))
    lista.append(inp)
print(f'O maior número é {max(lista)} e foi o', end=' ')
for c,v in enumerate(lista):
    if v == max(lista):
        cont_maior += 1
        if cont_maior > 1:
            print('e o ', end=' ')
        print(f'{c+1}º valor', end=' ')

print(f'\nO menor número foi {min(lista)} e foi o ', end=' ')
for c,v in enumerate(lista):
    if v == min(lista):
        cont_menor += 1
        if cont_menor > 1:
            print('e o ', end=' ')
        print(f'{c+1}º valor', end=' ')

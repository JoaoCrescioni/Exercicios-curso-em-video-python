nome_peso = list()
pessoas = list()
mai = men = 0
while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = nome_peso[1]
    else:
        if nome_peso[1] > mai:
            mai = nome_peso[1]
        if nome_peso[1] < men:
            men = nome_peso[1]
    pessoas.append(nome_peso[:])
    nome_peso.clear()
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Temos {len(pessoas)} pessoas cadastradas')
print(f' O maior peso foi {mai} Kg, pertencente a ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print(f' O menor peso foi {men} Kg, pertencente a ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ', end='')
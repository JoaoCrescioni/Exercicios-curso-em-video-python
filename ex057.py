sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Digite seu sexo (M/F): ')).upper().strip()[0]
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Digite um dado válido!')
print('Sexo registrado com sucesso!')
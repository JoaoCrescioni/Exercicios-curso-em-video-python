idade_geral = homem = mulher = 0
sexo = ''
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite seu sexo (M / F): ')).upper().strip()
    else:
        if idade > 18:
            idade_geral += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulher += 1
        cont = ' '
        while cont not in 'SsNn':
            cont = str(input('Quer continuar? (S / N): ')).upper()
        if cont == 'N':
            break
if idade_geral == 0:
    print('Todos são menores de idade!')
elif idade_geral == 1:
    print('Uma pessoa tem mais de 18 anos')
else:
    print(f'{idade_geral} pessoas tem mais de 18')
if homem == 0:
     print('Não há homens cadastrados')
elif homem == 1:
    print('Um homem foi cadastrado!')
else:
    print(f'{homem} homens foram cadastrados!')
if mulher == 0:
    print('Não há mulheres cadastradas com menos de 20!')
elif mulher == 1:
    print('Uma mulher com menos de 20 foi cadastrada !')
else:
    print(f'{mulher} com menos de 20 foram cadastradas!')
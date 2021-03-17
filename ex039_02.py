from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano-nascimento
tempo = [idade-18, 18-idade]

if nascimento > ano:
    print('Ano de nascimento inválido!')
else:
    if idade >= 18:
        if tempo[0] == 0:
            print('Sua data de alistamento é neste ano!')
        else:
            print('Sua data de alistamento já passou! Você esta {} anos atrasado!'.format(tempo[0]))
    else:
        if tempo[1] == 1:
            print('Você ainda não deve se alistar! Falta um ano!')
        else:
            print('Você ainda não deve se alistar! Faltam {} anos!'.format(tempo[1]))

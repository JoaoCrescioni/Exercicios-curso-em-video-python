import datetime
idade = int(input('Qual sua idade?: ').strip())

if idade == 18 :
    print('É hora de se alistar!!!')
elif idade == '': 
    print('Valor inválido!')
elif idade < 18 :
    print('Ainda não é hora de se alistar!!!')
    if 18 - idade == 1:
        print("Ainda falta 1 ano!!!")
    else:
        print("Ainda faltam {} anos!!!".format(18-idade))

else:
    print('Já passou da época de se alistar!!!')
    if idade-18 == 1 :
        print("Já se passou 1 ano do prazo!")
    else:
        print("Já se passaram {} anos do prazo!!!".format(idade-18))

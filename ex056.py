somaidade = 0
mediaidade = 0
menores20 = 0
maioridadehomem = []
nomehomem = []
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if sexo in 'Mm':
        maioridadehomem += [idade]
        nomehomem += [nome]
    if sexo in 'Ff' and idade < 20:
        menores20 += 1

junta_lista = zip(maioridadehomem, nomehomem)
sorteia_lista = sorted(junta_lista)
juncao = zip(*sorteia_lista)
maioridadehomem, nomehomem = [list(tuple) for tuple in juncao]


mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho é {} com {} anos!'.format(nomehomem[-1], maioridadehomem[-1]))
print('O número de mulheres com menos de 20 anos é {} !'.format(menores20))
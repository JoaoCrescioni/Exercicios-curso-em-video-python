tupla = ('Aprender', 'Programar', 'Entender', 'Estudar', 'Perder', 'Empatar', 'Esconder', 'Fugir')
for t in tupla:
    print(f'\nNa palavra {t.upper()} temos: ', end='')
    for letra in t:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
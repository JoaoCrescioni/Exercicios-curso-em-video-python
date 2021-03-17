tupla = ( int(input('Digite o primeiro número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição!')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares digitados foram:', end=' ')
for n in tupla:
    if n%2 == 0:
        print(n, end=' ')
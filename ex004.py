n1 = (input('Digite um número: '))
n2 = (input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))
print('É númerico?', s.isnumeric())
print('É composto apenas de letras? ', s.isalpha())
print('É composto de letras ou números? ',s.isalnum())
print('Está em letras maiúsculas? ', s.isupper())
print('Está em letras minúsculas? ', s.islower())
print('A que tipo pertence a variável?', type(s))

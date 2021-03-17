lista_pessoas = []
pessoa = {}
mulheres = []
media = 0
maior = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo[M/F]: '))
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    lista_pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Deseja continuar? [S/N] : '))
    if continuar in "Nn":
        break
for c in range(0, len(lista_pessoas)):
    media += lista_pessoas[c]['idade']
for c in range(0, len(lista_pessoas)):
    if lista_pessoas[c]['idade'] > media:
        maior.append(lista_pessoas[c]['nome'][:])

print(f'A) {len(lista_pessoas)} pessoas foram cadastradas!')
print(f'B) {media/len(lista_pessoas)} foi a média de idade ')
if len(mulheres) == 0:
    print('C) Não há mulheres cadastradas!')
elif len(mulheres) == 1:
    print(f'C) {mulheres} foi a mulher cadastrada!')
else:
    print(f'C) {mulheres} foram as mulheres cadastradas!')

print(f'D) {maior} foram as pessoas com idade maior que a média!')

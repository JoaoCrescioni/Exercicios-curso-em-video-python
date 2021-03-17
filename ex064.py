numero = cont = soma = 0
numero = int(input('Digite os números a serem somados: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite os números a serem somados: '))
print('A soma dos {} números digitados é {} !'.format(cont, soma))
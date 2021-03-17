nom = input('Insira aqui seu nome: ').strip()
nom2 = nom.split()
nom3 = nom.count(' ')
print('Seu primeiro nome é {} e seu último nome é {} '.format(nom2[0], nom2[nom3]))

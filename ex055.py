peso2 = []
for c in range (1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    peso2 += [peso]
    peso2.sort()

print('O menor peso é {} kg '.format(peso2[0]))
print('O maior peso é {} kg'.format(peso2[-1]))

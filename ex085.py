parimp = [[], []]
for c in range (1,8):
    parimp.append(int(input(f'Digite o {c}º valor: ')))
    if parimp[-1] % 2 == 0:
       parimp[0].append(parimp[-1])
    else:
        parimp[1].append(parimp[-1])
    parimp.pop(-1)
parimp[0].sort()
parimp[1].sort()
print(f'Os valores pares digitados foram: {parimp[0]}')
print(f'Os valores ímpares digitados foram: {parimp[1]}')

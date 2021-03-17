from datetime import date
s = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if date.today().year - ano < 18:
        s += 1
if s == 1:
    print('{} pessoa não alcançou a maioridade e 6 pessoas a alcançaram!!!'.format(s))
elif s==6:
    print('{} pessoas não alcançaram a maioridade e 1 alcançou!!'.format(s))
else:
    print('{} pessoas não alcançaram a maioridade e {} alcançaram!'.format(s,7-s))


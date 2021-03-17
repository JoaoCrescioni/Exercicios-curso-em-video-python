import datetime
ano = int(input('Qual o ano de nascimento do nadador? : '))

if datetime.date.today().year - ano <= 9:
    print('Você é um nadador mirim!')
elif datetime.date.today().year - ano <= 14:
    print('Você é um nadador infantil!')
elif datetime.date.today().year - ano <= 19:
    print('Você é um nadador júnior!')
elif datetime.date.today().year - ano < 25:
    print('Você é nadador sênior!')
else:
    print('Você é um nadador master!')

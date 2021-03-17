from datetime import datetime

dados = {}
dados['Nome'] = str(input('Digite seu nome: '))
dados['Nascimento'] = int(input('Digite seu ano de nascimento: '))
dados['Carteira'] = str(input('Você possui carteira de trabalho? [S/N] : '))
if dados['Carteira'] in "Ss" or "Simsim":
    dados['Contratação'] = int(input('Quando foi contratado? : '))
    dados['Salário'] = float(input('Qual seu salário? : '))
dados['Idade'] = datetime.today().year - dados['Nascimento']
dados['Aposentadoria'] = dados['Contratação'] + 35
for k,v in dados.items():
    print(f'{k} tem valor de {v}')

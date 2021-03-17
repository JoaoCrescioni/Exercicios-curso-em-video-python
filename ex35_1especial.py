nome = str(input('Qual seu nome?:').strip())

if nome.upper() == 'JOÃO':
    print('Seu nome, {}, é um dos melhores!'.format(nome))
elif nome == '' or nome == ' ' or len(nome) == 1:
    print('Você é bem misterioso, hein?')
else:
    print('É, {} é um nome bem estranho!!'.format(nome))

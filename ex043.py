peso = float(input('Digite seu peso: '))
altura = float(input('DIgite sua altura em metros: '))
imc = peso/altura**2
print('Seu IMC é de {:.2f} '.format(imc))
if imc < 18.5 :
    print('Você está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você está dentro da faixa de peso ideal')
elif 25 <= imc <= 30:
    print('Você tem sobrepeso')
elif 30 <= imc <= 40:
    print('Você tem obesidade')
else:
    print('Você tem obesidade mórbida!')
num = ('zero', 'um','dois','três','quatro','cinco',
       'seis','sete','oito','nove','dez',
       'onze','doze','treze','catorze','quinze',
       'dezesseis','dezessete','dezoito','dezenove','vinte' )
while True:
    num2 = int(input('Digite um número para vê-lo por extenso: '))
    if num2 < 0 or num2 >20:
        print('Digite um número válido!')
    else:
        print(f'O número {num2} por extenso fica {num[num2]}')
        seguir = str(input('Deseja seguir? [S/N]'))
        if seguir in 'Nn':
            break







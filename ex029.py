vel = float(input(" Velocidade lida: "))
if vel > 80:
    print('Você foi multado!')
    multa = (vel-80)*7
    print('Você tem de pagar R$ {:.2f} '.format(multa))
else:
    print('Você está dentro do limite!')

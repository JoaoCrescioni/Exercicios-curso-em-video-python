km = float(input('Insira a distância a ser percorrida (km) : ').strip())
if km <= 200:
    print('O total a pagar é R$ {:.2f} '.format(km*0.5))
else:
    print('O total a pagar é R$ {:.2f} '.format(km*0.45))

primeiro = int(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão da PA: '))
mais = int(input('Quer ver mais termos além do 10º? Quantos? ( se não, 0 ) '))
c = 1
if mais != 0:
    limite = 11 + mais
else:
    limite = 11
while c < limite:
    print('O {:.0f}º termo é {} !'.format(c, primeiro))
    c+=1
    primeiro *= razao

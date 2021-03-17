print('Cálculo de Empréstimo')
valor = float(input("Digite o valor da casa: ").strip())
sal = float(input('Digite o salário: ').strip())
dur = int(input('Digite por quantos anos vai pagar: ').strip())
prest = valor/(dur*12)

if prest > sal/100*30 :
    print('O valor da prestação excede 30% de seu salário, operação inválida!')
else:
    print("Seu empréstimo foi aprovado. As prestações serão de R$ {:.2f} por mês! ".format(prest))

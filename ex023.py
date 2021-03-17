num = int(input('Insira aqui um número (0~9999):'))

#print('A unidade é igual a: {}'.format(num[3]))
#print('A dezena é igual a: {}'.format(num[2]))
#print('A centena é igual a: {}'.format(num[1]))
#print('A milhar é igual a: ()'.format(num[0]))

u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('A unidade é igual a: {}'.format(u))
print('A dezena é igual a: {}'.format(d))
print('A centena é igual a: ()'.format(c))
print('A milhar é igual a: {}'.format(m))


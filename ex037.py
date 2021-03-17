num = int(input('Digite um número inteiro: '))
base = int(input('Escolha a base de conversão: 1 (bin), 2 (hex) ou 3 (oct): '))

if base == 1:
    print('O número {} convertido é igual a: {} ! '.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} convertido é igual a: {} ! '.format(num, hex(num)[2:]))
elif base == 3:
    print('O número {} convertido é igual a: {} ! '.format(num, oct(num)[2:]))

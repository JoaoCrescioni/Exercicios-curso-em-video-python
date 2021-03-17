opcao = 0
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
while opcao != 5:
    opcao = int(input('Qual operação você deseja realizar? \n'
    '[1] Somar\n'
    '[2] Multiplicar \n'
    '[3] Qual é maior?\n'
    '[4] Recomeçar!\n'
    '[5] Sair!\n'))
    if opcao == 1:
        print('A soma é: {}'.format(num2+num1))
    elif opcao == 2:
        print('O produto é: {}'.format(num2*num1))
    elif opcao ==3 and num1 > num2:
        print('O maior número é {} '.format(num1))
    elif opcao == 3 and num2 > num1:
        print('O maior número é {} '.format(num2))
    elif opcao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    else:
        print('Opção inválida! Tente novamente!')
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))

print('Fim das operações!')

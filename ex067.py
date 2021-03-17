while True:
    print('-'*20)
    num = int(input('Digite um número para ver sua tabuada!:'))
    print('-'*20)
    if num < 0:
        break
    for c in range (1,11):
        print(f'{c} X {num} = {c*num}')
print('ENCERRADO!')
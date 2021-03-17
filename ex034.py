sal = float(input('Digite seu ssalário para cálculo: '))

if sal > 1250:
    print('O aumento em seu salário será de R$ {} !'.format(sal/100*10))
else:
    print('O aumento em seu salário será de R$ {} !'.format(sal/100*15))

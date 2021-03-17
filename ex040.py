nota = float(input('Digite a primeira nota: ').strip())
nota2 = float(input('Digite a segunda nota: ').strip())

if (nota+nota2)/2 < 5 :
    print('Média abaixo do esperado, {:.2f}. Reprovado!'.format((nota+nota2)/2))
elif (nota+nota2)/2 > 7 :
    print('Parabéns pela nota {:.2f} ! Aprovado'.format((nota+nota2)/2))
elif nota < 0 or nota2 < 0 or nota > 10 or nota2 > 10:
    print('Valor inválido inserido!')
else:
    print('Valor médio obtido de {:.2f} . Recuperação!'.format((nota+nota2)/2))

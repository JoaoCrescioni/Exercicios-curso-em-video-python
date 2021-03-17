exp = str(input('Digite uma expressão númerica: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta!')

#if exp.count('(') == exp.count(')'):
#   print('Essa expressão é válida!')
#else:
#   print('Essa expressão é inválida!')
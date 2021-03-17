fr1 = input('Insira um frase aqui: ').strip().lower()
fr2 = fr1.lower()
print('A frase tem {} letras ´a´ \n A primeira aparece na {}º posição e a última na {}º posição '.format(fr2.count('a'),fr2.find('a')+1, fr2.rfind('a')+1))


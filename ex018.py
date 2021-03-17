import math
catop = float(input("Insira aqui o cateto oposto: "))
catad = float(input("Insira aqui o cateto adjacente: "))
print(" Com base nos catetos informados, a hipotenusa é: {}".format(math.hypot(catad, catop)))

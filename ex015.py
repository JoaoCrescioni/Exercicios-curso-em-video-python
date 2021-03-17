dias = int(input("Insira o número de dias em que o carro foi alugado:"))
km = float(input("Insira o número de quilômetros rodados com o carro: "))
print(" O valor total a ser pago é {:.2f} R$".format(dias*60+km*0.15))

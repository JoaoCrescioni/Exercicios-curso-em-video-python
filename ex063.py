primeiro = int(input('Digite um número para iniciar a sequência: '))
final = int(input('Digite quantos termos você quer ver: '))
c = 1
seq = 0
while c < final+1:
    print('O {:.0f}º termo é {} !'.format(c, primeiro))
    seq = primeiro - seq
    c += 1
    primeiro += seq

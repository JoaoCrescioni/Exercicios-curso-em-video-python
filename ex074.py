from random import randint as int
num = (int(0,100), int(0,100), int(0,100), int(0,100), int(0,100))
print(num)
menor = num[0]
for c in range(1,5):
    if menor > num[c]:
        menor = num[c]
maior = num[0]
for x in range(1,5):
    if maior < num[x]:
        maior = num[x]
print(f'O menor número é {menor} e o maior é {maior}')
# {max(num)}
# {min(num)}
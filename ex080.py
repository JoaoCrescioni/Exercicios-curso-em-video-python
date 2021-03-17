num_list = []
for c in range (0,5):
    num_list.append(int(input('Digite um número: ')))
    if len(num_list) == 1:
        print(f'O número {num_list[0]} foi adicionado e iniciou a lista!')
    else:
        if num_list[c] > num_list[c-1]:
            print(f'O número foi adicionado ao final da lista! ')


        if num_list[c] < num_list[0]:
            print(f'O número foi adicionado ao início da lista!')
        if len(num_list) >=3:
            if num_list[0] < num_list[-1] < num_list[-2]:
                print(f'O número foi adicionado no meio da lista! ')

        num_list.sort()
print(num_list)


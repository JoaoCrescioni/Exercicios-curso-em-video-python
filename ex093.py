estat = {}
gols = []
estat['nome'] = str(input('Qual o nome do jogador? : '))
estat['partidas'] = int(input(f'Quantas partidas {estat["nome"]} jogou? : '))
for c in range(0, estat['partidas']):
    gols.append(int(input(f'Quantos gols {estat["nome"]} fez na {c+1}º partida? : ') ))
estat['gols'] = gols.sort()
print(f'O jogador {estat["nome"]} jogou {estat["partidas"]} partidas! Nelas, fez...')
for c in range(0, estat['partidas']):
    print(f'    ==> Na {c+1}ª partida, fez {gols[c]} gols ')
print(f'Foi um total de {sum(gols)} gols!')
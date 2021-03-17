cid = input('Digite o nome da cidade: ').strip()
cid2 = cid.split()
cid3 = 'SANTO' in cid2[0].upper()
print('A cidade começa com ´Santo´?: {} '.format(cid3))

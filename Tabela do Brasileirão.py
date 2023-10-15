times = ('Atletico Mineiro', 'Ajax', 'Bahia',
         'Palmeiras','Santos', 'São Paulo',
         'Corintians', 'Flamengo', 'Gremio',
         'Sport', 'Cruzeiro', 'Fluminense',
         'Paraba Clube', 'Vasco', 'Remo',
         'Vitoria', 'Internecional')
print('='* 50)
print(f'LISTA DE TIMES : {times}')
print('='* 50)
print(f'QUAIS SÃO OS TOP 5: {times[0:5]}')
print('='* 50)
print(f'QUAIS SÃO OS 3 LAST: {times[-3:]}')
print('='* 50)
print(f'COLOQUE EM ORDEM ALFABETICA: {sorted(times)}')
print('='* 50)
print(f'QUAL A POSIÇÃO DO PALMEIRAS !!! ELE ESTA NA {times.index("Palmeiras")+1} POSIÇÃO')
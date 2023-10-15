print('GERADOR DE PA')
print('=+='*60)
primeiro = int(input('PRIMEIRO TERMO:  '))
razão =  int(input('RAZÃO DA PA:  '))
termo = primeiro
contador = 1
while contador <= 10:
    print( '{} -> '.format(termo), end='')
    termo += razão
    contador += 1
print('FIM !!!!!!')



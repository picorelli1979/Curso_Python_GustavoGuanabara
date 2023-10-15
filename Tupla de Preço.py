listagem = ('Caderno', 12.50,
            'Classificador', 7.50,
            'Lápis', 2.50,
            'Grafite' , 8.00,
            'Prancheta', 12.50,
            'Mochila', 120.00)
print ('='* 35)
print (f'{"LISTA DE MATERIAIS ESCOLARES":^35}')
print ('='* 35)
for pos in range (len(listagem)):
    if pos % 2 == 0:
       print(f'{listagem[pos]:.<25}', end='')
    else:
        print (f'R$ {listagem[pos]:>5.2f}')
print ('='* 35)

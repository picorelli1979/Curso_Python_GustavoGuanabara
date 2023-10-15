palavras = ('alpha', 'carro', 'sol',
            'sombra', 'tesoura', 'amar',
            'lapis', 'xicara', 'copo',
            'caderno', 'praia', 'terremoto')
print( '=' * 35)
print(f'{"INDENTIFIQUE AS VOGAIS":^30}')
print( '=' * 35)
for p in palavras:
    print( f'\nNa palavra {p.upper()} tem essas vogais:  ', end='')
    for letra in p:
        if letra.lower() in 'a e i o u':
            print(letra,end = '')
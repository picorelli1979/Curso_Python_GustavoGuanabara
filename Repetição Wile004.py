print('GERADOR DE PA')
print('=+='*60)
primeiro = int(input('PRIMEIRO TERMO:  '))
razão =  int(input('RAZÃO DA PA:  '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ->'.format(termo), end='')
        termo += razão
        contador += 1
    print('PAUSA...')
    mais = int(input('Quantos termos você quer mostrar a mais?  '))

print('Progressão foi Finalizada com {} termos'.format(total))
print('FIM')


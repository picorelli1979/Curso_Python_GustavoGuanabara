frase = str(input('Digite uma frase:  ')).upper()
print('Quantas vezes apareceu a letra:{}'.format(frase.count('A')))
print('A letra A aparece primeiro na posição: {}'.format(frase.find('A')+1))
print('Em que posição a letre A aparece por ultimo: {}'.format(frase.rfind('A')+1))
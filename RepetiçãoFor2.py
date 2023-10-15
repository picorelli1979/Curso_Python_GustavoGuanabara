print('APRESENTE OS NUMEROS MULTIPLOS DE 3 E SUA SOMA  !!!')
print('='*60)
soma = 0
cont = 0
for n in range (1,501,2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
print('A SOMA DOS {} VALORES É {}'.format(cont,soma))

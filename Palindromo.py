frase= str(input('DIGITE UMA FRASE:   ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if  inverso == junto:
    print('ESTA FRASE É UM POLINDROMO !!!!')
else:
    print('ESTÁ FRASE NÃO É UM POLINDROMO.....')

print('Escrito isso {} de trás pra frente fica{}'.format(junto,inverso))


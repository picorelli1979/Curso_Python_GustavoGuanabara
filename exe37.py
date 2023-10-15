print('='*30)
print('ANALISADOR DE TRIANGULO')
print('='*30)

t1 = float(input('Primeiro Segmento:   '))
t2 = float(input('Segundo Segmento:    '))
t3 = float(input('Terceiro Segmento:   '))

if t1 < t2 + t3 and t2 < t1 +t3 and t3 < t2 + t3:
    print('Este resultado PODE SER UM TRIANGULO')
else:
    print('Este resultado NÃO PODE FORMAR UM TRINGULO')

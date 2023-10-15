from datetime import date

atual = date.today().year
nascimento = int(input('DIGITE SEU ANO DE NASCIMENTO:  '))
idade = atual - nascimento

print('Sua idade é {}'.format(idade))

if idade <= 9:
    print('Categoria MIRIN')

elif idade <= 14:
    print('Categoria INFANTIL')

elif idade <= 19:
    print('Categoria JUNIOR')

elif idade <= 25:
    print ('Categoria SENIOR')

else:
    print('Categoria MASTER')
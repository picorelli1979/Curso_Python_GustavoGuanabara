n1 = float(input('Nota Primeira Unidade:  '))
n2 = float(input('Nota Segunda Unidade:   '))
m = (n1 + n2)/2

print('Sua media é {}'.format(m))
if m > 6.0:
    print("Você está APROVADO")
else:
    print('Está REPROVADO')
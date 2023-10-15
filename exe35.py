a = int(input('Digite o Primeiro Número:  '))
b = int(input('Digite o Segundo Número:   '))
c = int(input('Digite o Terceiro Número:  '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado no terminal foi {}'.format(menor))
print('O maior valor digitado no terminal foi {}'.format(maior))

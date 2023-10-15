somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20tot = 0

for p in range (1,5):
    print('========== {} PESSOA =========='.format(p))
    nome = str(input('NOME:  ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:  ')).strip()
    somaidade += idade
    
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in 'Ff' and idade < 20:
        mulher20tot += 1
médiaidade = somaidade / 4

print('A média de idade do Grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos! E se chama-se: {}'.format(maioridadehomem,nomevelho))
print('Existem {} mulheres com menos de 20 anos'.format(mulher20tot))
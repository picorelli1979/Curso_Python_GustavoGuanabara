nome= str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print(nome)
print('Prazer em te conhecer  {} !'.format(nome[0]))
print('Qual o seu ultimo nome?')
print('Meu ultimo nome é {}'.format(nome[len(nome)-1]))


nome = str(input('Digite seu nome: ')).strip()

if nome =='Fabricio':
    print('Você tem um belo nome')

elif nome == 'Kalleo'or nome == 'Micael':
    print('Legal seu Nome é bem diferente !!!!')

elif nome == 'Pedro' or nome== 'Maria' or nome== 'Ana' or nome== 'Carlos':
    print('Seu nome é bem popular......')

else:
    print(' \033[1;31;107mSEU NOME ESTÁ FORA DA LISTA DE CONVIDADOS\033[m')
print('Seja Muito Feliz')
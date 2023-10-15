n = int(input("Digite um Numero:"))
a = n - 1
s = n + 1
h = n * 10
print('\033[1;34;43m Analisando o valor {} seu antecessor será {} e seu sucessor será {}\033[m'.format(n,a,s))
print('Qual será o valor {} multiplicado por 10 ? Ele será {}'.format(n,h))
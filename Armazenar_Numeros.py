n = int(input('Digite um Numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} é {} '.format(n, d))
print('O triplo de {} é {} '.format(n, t) ,end='')
print('A raiz de {} é {:.3f} '.format(n, r))
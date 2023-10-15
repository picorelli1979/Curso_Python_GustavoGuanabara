num=int(input ('Digite um número:  '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('UNIDADE: {}'.format(u))
print('DEZENA:  {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR:  {}'.format(m))

# ESSE EXERCICIO TEVE 2 MANEIRAS DE FAZER
#n=str(num)
#print('UNIDADE : {}'.format(n[3]))
#print('DEZENA:   {}'.format(n[2]))
#print('CENTENA:  {}'.format(n[1]))
#print('MILHAR:   {}'.format(n[0]))
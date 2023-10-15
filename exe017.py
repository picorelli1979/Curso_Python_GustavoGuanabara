import math
Cop = float(input('QUAL O CUMPRIMENTO: '))
Cad = float(input('QUAL O CUMPRIMENTO: '))

hip = math.hypot(Cop,Cad)

print('O valor da hipotenusa é {:.2f}'.format(hip))
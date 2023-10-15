A = float(input('Qual á a altura da parede?:'))
L = float(input('Qual a largura da parede?:'))
área = A * L
tinta = área / 2

print("A sua parede tem {:.2f} x {:.2f} sendo sua área total de {:.2f} m2".format(A, L, área))
print('Sendo assim eu preciso de {:.2f} de Litros de tinta'.format(tinta))



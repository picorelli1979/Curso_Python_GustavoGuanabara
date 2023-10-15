real = float(input('Quanto vc tem na carteira?: R$'))

dolár= real / 5.50
euro = real / 6.26
iene = real / 0.048


print('Com R$ {} equivale há U$${:.2f} Dolares'.format(real, dolár))
print('Com R$ {} equivale há ${:.2f} Euros'.format(real, euro))
print('Com R$ {} equivale há ${:.2f} Ienes'.format(real, iene))




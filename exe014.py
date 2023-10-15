produto = float(input('\033[1;97;41mQual o valor deste produto ?:R$  '))
desc = produto * 10/100
vr = produto - desc

print('O valor do desconto é de  R$ {:.2f}' .format(desc))
print('Valor a ser pago já com desconto é R$ {:.2f}'.format(vr))
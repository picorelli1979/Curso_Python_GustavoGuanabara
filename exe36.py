salario = float(input("Digite seu atual salario:    "))
if salario <= 1200:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print(" Com o aumento de salario, hj seu salario que é {:.2f} passará a ser {:.2f}".format(salario,novo))


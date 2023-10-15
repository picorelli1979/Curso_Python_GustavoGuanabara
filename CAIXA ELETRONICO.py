print('='*50)
print('{:^40}'.format('CAIXA ELETRONICO 24h'))
print('='*50)

valor = int(input('VALOR DO SAQUE: R$    '))
total = valor
cedu = 100
totcedu = 0

while True:
    if total >= cedu:
       total -= cedu
       totcedu += 1
       
    else:
        if totcedu > 0:
            print(f'TOTAL DE {totcedu} cedulas de R${cedu}')
        
        if cedu == 100:
            cedu = 50
            
        elif cedu == 50:
            cedu = 20
            
        elif cedu == 20:
            cedu = 10
            
        elif cedu == 10:
            cedu = 5
            
        elif cedu == 2:
            cedu = 2
            
        elif cedu == 1:
            cedu = 1
            
        totcedu = 0
        
        if total == 0:
            break
print('='*50)
print('VOLTE SEMPRE!!!')
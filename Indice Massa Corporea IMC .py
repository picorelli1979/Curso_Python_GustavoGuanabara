peso = float(input('QUAL É O SEU PESO ?    (kg)'))
altura = float(input('QUAL A SUA ALTURA ?   (m)')) 
imc = peso / (altura**2)

print('O SEU IMC É {:.1f}'.format(imc))

if imc < 20 :
    print('Você está muito abaixo do peso, PERIGO !!!!')

elif 21 <=  imc <= 30 : 
    print('Você continua abaixo do peso, CONTINUE SE DEDICANDO !!!')

elif 31 <= imc < 50 :
    print ('Você está com SOBREPESO... CUIDADO !!!')  
else :
    print('Você está com OBSIDADE MORBIDA..... DIRIJA-SE AO MÉDICO')    
   
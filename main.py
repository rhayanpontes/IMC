altura = float(input('Digite a sua altura :'))
peso = float(input('Digite o seu peso :'))

imc = peso / (altura * altura)
print('Seu IMC é %.2f:' % imc)

if(imc < 18.5):
    print('Você esta abaixo do peso')
elif(imc <= 24.9):
    print('Voce esta no peso ideal')
elif(imc <= 29.0):
    print('Voce esta com sobrepreso')
elif(imc <=39.0):
    print('Você esta com obesidade')
elif(imc >=40.0):
    print('Você esta com obesidade grave')

print('Aconselhamos você a se hidratar, por esse motivo \nvamos lhe informar quantos Litros precisa beber por dia.')
lpd = peso * 0.035
print('Você precisa beber %2.f' % lpd + 'L pro dia')
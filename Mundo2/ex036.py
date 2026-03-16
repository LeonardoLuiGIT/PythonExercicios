""" Escreva um programa para aprovar o emprestimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo
será negado.
"""

#Solicita o valor da casa, do salário e os anos a ser pago.
print('-=-'* 20)
print('EMPRESTIMO')
print('-=-' * 20)
valCasa = float(input('Digite o valor da casa: R$'))
valSal = float(input('Digite o seu salário: R$'))
anos = float(input('Anos a ser pago:  '))

#Descobrindo o valor da prestação mensal
meses = 12 * anos
prestMes = valCasa / meses

#Calcula 30% do salário
salNovo = valSal * 0.30

#Verificar se o emprestimo será aprovado ou negado.
if prestMes <= salNovo:
    print('Valor do emprestimo: R${:.2f} '.format(prestMes))
    print('Status: Aprovado! ✅ ')
else:
    print('Valor do emprestimo: R${:.2f} '.format(prestMes))
    print('Status: Negado! ❌ ')
#print('O valor da prestação mensal é: {}'.format(prestMes))


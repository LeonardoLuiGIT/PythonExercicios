#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou igual, o aumento é de 15%

sal = float(input("Informe o salário do funcionário: "))

if sal > 1250:
    aumento = sal + (sal * 10 / 100)
    print("Seu salário de R${}, teve aumento de 10%, ficando R${:.2f}".format(sal, aumento))
else:
    aumento = sal + (sal * 15 / 100)
    print("Seu salário de R${}, teve aumento de 15%, ficando R${:.2f}".format(sal, aumento))

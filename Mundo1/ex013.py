#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s1 = float(input('Qual o salário atual do funcionário? R$'))
pro = s1 + (s1 * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(s1,pro))
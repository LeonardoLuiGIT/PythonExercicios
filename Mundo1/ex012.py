#Faça um algoritmo que çeia o preço de um produto e mostre seu novo preço, com 5% de desconto
nome = input('Qual o nome do produto? ')
pr = float(input('Qual o preço do produto? R$ '))
des = pr - (pr * 5) / 100
print('{} que custava R${}, na liquidição de 5%, sai por R${:.2f}'.format(nome, pr, des))
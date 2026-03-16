#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

#Importa a biblioteca Maht
import math

#Lê o número como float
num = float(input('Informe um número real qualquer: '))

#Imprime o número de forma inteira
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))
#Faça um programa que leia um número e mostre na tela cada ums dígitos separados.

#Lê o número informado
numero = (input("Informe um número de 0 a 9999: "))

#Imprime a unidade do número
print("Unidade: {}".format(numero[0]))

#Imprime a dezena do número
print("Dezena: {}".format(numero[1]))

#Imprime a centena do número
print("Centena: {}".format(numero[2]))

#Imprime o milhar do número
print("Milhar: {}".format(numero[3]))
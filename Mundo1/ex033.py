#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

maior = num1
menor = num1

#Verificando quem é o maior
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

#Verificando quem é o menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O número maior é {}".format(maior))
print("O número menor é {}".format(menor))
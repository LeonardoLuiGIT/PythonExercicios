#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
#podem ou não formar um triângulo.

print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)
r1 = float(input("Informe o comprimento da primeira reta: "))
r2 = float(input("Informe o comprimento da segunda reta: "))
r3 = float(input("informe o comprimento da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("É possível formar um triângulo com essas retas!")
else:
    print("Não é possível formar um triângulo com essas retas!")
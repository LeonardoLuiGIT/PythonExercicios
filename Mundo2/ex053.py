"""Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsierando os espaços"""

frase = input("Digite uma frase: ").lower().strip()
frase = frase.replace(" ", "")

invertida = ""

for letra in frase:
    invertida = letra + invertida

if frase == invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
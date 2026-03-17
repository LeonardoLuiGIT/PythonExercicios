"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

menor_peso = 999
maior_peso = 0


for c in range(5):
    peso = int(input('Digite o seu peso: KG '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso é {maior_peso}!')
print(f'O menor peso é {menor_peso}!')

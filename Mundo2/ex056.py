"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos."""
from time import sleep

soma = 0
mais_velho = 0
nome_mais_velho = ''
mulheres_menos_20 = 0

for c in range(4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').upper()
    sleep(1)
    print('Dados coletados, próximo! ')

    soma += idade

    if sexo == 'M':
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1


media = soma / 4

print(f'A média das idades é {media}!')
print(f'O nome do homem mais velho é o {nome_mais_velho}!')
print(f'A quantidade de mulheres, com menos de 20 anos é {mulheres_menos_20}! ')
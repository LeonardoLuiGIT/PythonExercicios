"""Crie um programa que leia o ano de nascimento de sete pessoas. No Final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores"""

from datetime import date

data = date.today().year

maiores = 0
menores = 0
mais_velho = 0
mais_novo = 999

for c in range(7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = data - ano
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
    if idade > mais_velho:
        mais_velho = idade
    if idade < mais_novo:
        mais_novo = idade

print(f'Total de maiores de idade: {maiores} pessoas!')
print(f'Total de menores de idade: {menores} pessoas! ')
print(f'Pessoa mais velha: {mais_velho} anos')
print(f'Pessoa mais nova: {mais_novo} anos')
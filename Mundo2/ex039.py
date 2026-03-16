""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo de alistamento
"""
from datetime import date

print('-=-'* 20)
print('Site do Exército')
print('-=-' * 20)

#Solicita o ano de nascimento do usuário
ano = int(input('Digite o ano de nascimento: '))

#Armazena o ano atual (2026) na variavel ano_atual, para calcular a idade do usuário
ano_atual = date.today().year
idade = ano_atual - ano

#Informa se já passou, se ainda falta ou está na hora de se alistar, e imprime a mensagem na tela.
if idade > 18:
    idade1 = idade - 18
    print(f'Já passou {idade1} anos do prazo de se alistar! ')
elif idade < 18:
    idade1 = 18 - idade
    print('Você ainda vai se alistar ao serviço militar! ')
    print(f'Ainda faltam {idade1} anos para você se alistar! ')
else:
    print('Está na hora de se alistar! ')
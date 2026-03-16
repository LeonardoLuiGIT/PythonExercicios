""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo de alistamento
"""

print('-=-'* 20)
print('SITE DO EXÉRCITO')
print('-=-' * 20)

idade = int(input('Informe sua idade: '))

if idade > 18:
    idade1 = idade - 18
    print(f'Já passou {idade1} do prazo de se alistar! ')
elif idade < 18:
    idade1 = 18 - idade
    print('Você ainda vai se alistar ao serviço militar! ')
    print(f'Ainda faltam {idade1} anos para você se alistar! ')
else:
    print('Está na hora de se alistar! ')

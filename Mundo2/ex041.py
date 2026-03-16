""" A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

print('-=-'* 20)
print('Site da Confederação Nacional de Natação')
print('-=-' * 20)

ano = int(input('Digite o ano do seu nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print(f'Você possui {idade} anos, se enquadra na categoria Mirim! ')
elif 9 < idade <= 14:
    print(f'Você possui {idade} anos, se enquadra na categoria Infantil! ')
elif 14 < idade <= 19:
    print(f'Você possui {idade} anos, se enquadra na categoria Junior! ')
elif 19 < idade <= 20:
    print(f'Você possui {idade} anos, se enquadra na categoria Sênior! ')
else:
    print(f'Você possui {idade} anos, se enquadra na categoria Master! ')
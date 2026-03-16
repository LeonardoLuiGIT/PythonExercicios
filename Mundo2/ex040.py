""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÂO
- Média 7.0 ou superior:
APROVADO
"""

print('-=-'* 20)
print('Leitor de média')
print('-=-' * 20)

nota1 = float(input('Informe a primeira nota do Aluno: '))
nota2 = float(input('Informe a segunda nota do Aluno: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'A média do aluno foi {media:.2f}, e está reprovado! ')
elif 5 <= media <= 6.9:
    print(f'A média do aluno foi {media:.2f}, e está de recuperação! ')
else:
    print(f'A média do aluno foi {media:.2f}, e está aprovado! ')
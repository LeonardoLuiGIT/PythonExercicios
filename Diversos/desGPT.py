from time import sleep

mais_velho = 0
nome_mais_velho = ''
maior_salario = 0
soma_salarios = 0
salarios = []

for c in range(3):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = int(input('Digite seu salário: '))
    sleep(1)
    print('Dados coletados, próximo! ')

    soma_salarios += salario
    salarios.append(salario)

    if idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome

    if salario > maior_salario:
        maior_salario = salario

media = soma_salarios / 3

abaixo_media = 0
for s in salarios:
    if s < media:
        abaixo_media += 1

print(abaixo_media)
print(media)
print(nome_mais_velho)
print(maior_salario)
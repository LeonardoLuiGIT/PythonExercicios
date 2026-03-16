#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = input('Nome do aluno: ')
n1 = float(input('Informe a primeira nota do {}: ' .format(nome)))
n2 = float(input('Informe a segunda nota do {}: ' .format(nome)))
m = (n1 + n2) / 2
print('A média do aluno {} é {}'.format(nome, m))
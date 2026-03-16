#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
#o nome deles e escrevendo o nome do escolhido

#Importa a biblioteca Random, para sortear os nomes.
import random

# Lê os nomes dos alunos
nome = input("Digite o nome do primeiro aluno: ")
nome1 = input("Digite o nome do segundo aluno: ")
nome2 = input("Digite o nome do terceiro aluno: ")
nome3 = input("Digite o nome do quarto aluno: ")

#Cria uma variável que agrupa os nomes dos alunos
alunos = [nome, nome1, nome2, nome3]

#Mostra na tela, qual o aluno escolhido
print("O aluno escolhido para apagar o quadro foi {}".format(random.choice(alunos)))


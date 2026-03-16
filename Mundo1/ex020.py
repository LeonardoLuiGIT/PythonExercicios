#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada

#Importa a biblioteca Random
import random

#Lê o nome dos alunos
nome1 = input("Informe o nome do primeiro aluno: ")
nome2 = input("Informe o nome do segundo aluno: ")
nome3 = input("Informe o nome do terceiro aluno: ")
nome4 = input("Informe o nome do quarto aluno: ")

#Agrupa os alunos, numa única variável
aluno = [nome1, nome2, nome3, nome4]

#Faz com que seja embaralhado os nomes dos alunos
random.shuffle(aluno)

#Imprime na tela a ordem dos alunos
print("A ordem de apresentação será: {}".format(aluno))
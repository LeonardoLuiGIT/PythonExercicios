#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao (Sem considerar espaços)
#Quantas letras tem o primeiro nome

#Lê o nome informado pelo utilizador
frase = input("Qual o seu nome inteiro? ").strip()

#Cria uma variável com a frase dividida
dividido = frase.split() #

#O nome com todas as letras maiúsculas
print("Nome em maiúsculo: {}.".format(frase.upper()))

#O nome com todas as letras minúsculas
print("Nome em minúsculo: {}.".format(frase.lower()))

#Quantas letras ao (Sem considerar espaços)
print("Seu nome possui {} letras.".format(len(frase.replace(" ", ""))))

#Quantas letras tem o primeiro nome
print("Seu primeiro nome, possui {} letra.".format(len(dividido[2])))

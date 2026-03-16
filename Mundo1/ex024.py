#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santos"

#Lê o nome da cidade
cidade = input("Informe o nome de uma cidade: ").strip()

#Imprime True caso tenha Santos, false se não tiver
print("Começa com Santos? {}".format(cidade.startswith("Santos")))
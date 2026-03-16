#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Informe seu nome inteiro: ").strip()

# Divide o nome numa lista de palavras
nomes = nome.split()

# Obtém o primeiro e o último nome
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
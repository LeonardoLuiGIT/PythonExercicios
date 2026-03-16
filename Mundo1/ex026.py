#Faça um programa que leia uma frase peo teclado e mostre
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input("Digite uma frase: ").strip()
vezes = frase.count("a")
primeira = frase.find("a")
ultima = frase.rfind("a")
print(f"A letra A aparece {vezes} vezes. \n A primeira vez que a letra A é na posição {primeira}. \n A última vez que a letra A aparece é na posição {ultima} ")
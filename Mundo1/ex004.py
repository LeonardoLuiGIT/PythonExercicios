#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possível sobre ele.
n = input("Digite algo: ")
print("\033[1:35:42mO tipo primitivo desse valor é " , type(n))
print("\033[4:33:44mEstá tudo em máisculo?" , n.isupper())
print("Está tudo em minúsculo?" , n.islower())
print("Possui somente espaços?", n.isspace())
print("É somente númerico? " , n.isnumeric())
print("É somente alfabético? " , n.isalpha())
print("É alfanúmerico?" , n.isalnum())
print("Está capitalizada?" , n.istitle())

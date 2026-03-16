#Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random #Importa a biblioteca random
import time
from time import sleep

num = random.randint(0,5) #Armazena na variável num, um número de 0 a 5
print("-=-" * 20)
print("Vou pensar em um número entre 0 a 5. Tente adivinhar....")
print("-=-" * 20)
num2 = int(input("Em que número eu pensei? ")) #Solicita ao usuário, que tente adivinha o número de 0 a 5
print("Processando...")
sleep(3)
if num == num2:
    print("Parabéns! Você acertou :D") #Se o usuário acertar o número escolhido
else:
    print("Você errou! :(") #Se o utilizador não acertar
    print("O número escolhido foi {}".format(num)) #Imprime no fim, o número que o sistema escolheu
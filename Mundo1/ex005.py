#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
#e seu antecessor.
n1 = int(input('Escolha um número: '))
s = n1 + 1
m = n1 - 1
print('O antecessor de {} é {} \n O sucessor de {} é {}'.format(n1, m, n1, s))
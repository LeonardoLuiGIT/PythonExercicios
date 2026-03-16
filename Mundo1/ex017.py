#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangilo, calcule
#e mostre o comprimento da hipotenusa

#Importa da biblioteca math, somente o comando hypot
from math import hypot

#Lê os catetos informados pelo utilizador
catetoOposto = float(input('Qual o comprimento do cateto oposto? '))
catetoAdj = float(input('Qual o comprimento do cateto adjacente? '))

#Faz o calculo da hipotenusa
hipo = hypot(catetoOposto,catetoAdj)

#Imprime na tela o resultado e demais informações
print('Um triângulo retângulo, com um cateto oposto de {}cm e um cateto adjacente de {}cm, possui a hipotenusa a {:.2f}cm.'.format(catetoOposto,catetoAdj,hipo))
#Faça um programa que leia um ângulo qualquer e mostre na tela, o valor do seno, cosseno e tangente desse ângulo
import math
# Solicita o grau para o usuário
angulo = float(input('Informe o grau de qualquer ângulo: '))

# Converte o grau do utilizador (float) em grau (radiano)
grau = math.radians(angulo)

# Realiza os cálculos, seno, cosseno e tangente
cos = math.cos(grau)
tang = math.tan(grau)
seno = math.sin(grau)

# Imprime na tela, o resultado de cada um
print('O ângulo de {}°, possui um seno de {:.2f}°, um cosseno de {:.2f}° e uma tangente de {:.2f}°.'.format(angulo, seno, cos, tang))
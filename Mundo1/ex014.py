#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
celsius = float(input('Quantos graus está fazendo, em Celsius? '))
fah = (celsius * 9/5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(celsius, fah))
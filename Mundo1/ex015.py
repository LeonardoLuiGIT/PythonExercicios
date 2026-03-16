#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado
dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KMs o carro percorreu? '))
preco = (60 * dia) + (km * 0.15)
print('O preço a pagar pelo carro, que foi usado por {} dias e percorrido {}km, é de R${}'.format(dia, km, preco))

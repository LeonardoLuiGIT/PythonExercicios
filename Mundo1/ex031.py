#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço
#da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.

dist = int(input("Informe a distancia da viagem: "))

if dist <= 200:
    valor = 0.50 * dist
else:
    valor = 0.45 * dist
print("Uma viagem de {}Km, custa R${}.".format(dist, valor))
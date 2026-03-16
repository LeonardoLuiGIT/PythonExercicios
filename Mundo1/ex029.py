#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
#que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite

vel = float(input("Digite a velocidade do veículo: "))

limite = 80

if vel > limite:
    excesso = vel - limite
    multa = excesso * 7
    print("Você ultrapassou o limite de {}Km e foi multado em R${}!".format(limite, multa))
else:
    print("Velocidade dentro do limite, dirija com cuidado!")
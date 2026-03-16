#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
r = float(input('Quantos reais você possui? R$'))
d = r / 3.27
euro = r / 6.11
print('Com R${}, você pode comprar US${:.2f}'.format(r, d))
print('Com R{}, você pode comprar EU${:.2f}'.format(r, euro))
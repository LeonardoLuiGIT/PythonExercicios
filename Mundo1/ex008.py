#Escreva um programa que leia um valor em metros e o exiba em centímetro e milímetros
n1 = float(input('Informe um valor em metros: '))
cm = n1 * 100
mm = n1 * 1000
km = n1 / 1000
hm = n1 / 100
dm = n1 * 10
print("{}m é {}cm \n {}m é {}mm \n {}m é {}km \n {}m é {}hm \n {}m é {}dm".format(n1, cm, n1, mm, n1, km, n1, hm, n1, dm))
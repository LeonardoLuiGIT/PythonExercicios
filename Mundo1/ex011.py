#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
ar = l * a
q = ar / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l,a, ar))
print('É necessário {} litros de tinta para pintar uma área de {}m.²'.format(q, ar))

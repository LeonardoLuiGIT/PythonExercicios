#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada
#n1 = int(input('Informe um número: '))
#d = n1 * 2
#t = n1 * 3
#rq = n1**(1/2)
#print('O dobro de {} é {} \n O triplo de {} é {} \n A raíz quadrada de {} é {:.2f}' .format(n1, d, n1, t, n1, rq))

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raíz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))
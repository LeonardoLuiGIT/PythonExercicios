""" Refaça o Desafio 035 dos triângulos, acrescentendo o recurso de mostrar
que tipo de triângulo será formado
- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""

print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)
r1 = float(input("Informe o comprimento da primeira reta: "))
r2 = float(input("Informe o comprimento da segunda reta: "))
r3 = float(input("informe o comprimento da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("É possível formar um triângulo com essas retas!")

    if r1 == r2 == r3:
        print('Será formado um triângulo equilátero! ')

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Será formado um triângulo isósceles! ')

    else:
        print('Será formado um triângulo escaleno! ')

else:
        print("Não é possível formar um triângulo com essas retas!")
""" Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando o laço for."""

num = int(input("Digie um número: "))

for c in range(1, 11):
    res = num * c
    print(f'{num} x {c} = {res}')
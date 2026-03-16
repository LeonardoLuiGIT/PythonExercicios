"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles forem pares.
Se o valor digitado for impar, desconsidere-o"""

s = 0
for c in range(1, 7):
    num = int(input("Digite um número:"))
    if num % 2 == 0:
        s += num
print(f"A soma dos pares é {s}")

""" Desenvolve uma lógia que leia o peso e a altura de uma pessoa, calcule seu
IMC e mostre seu status, de acordo com a tabela abaixo
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5  e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

print("-=-" * 20)
print("Calculadora de IMC")
print("-=-" * 20)

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, e seu status é Abaixo do Peso! ')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é {imc:.2f}, e seu status é Peso Ideal! ')
elif 25 < imc <= 30:
    print(f'Seu IMC é {imc:.2f}, e seu status é Sobrepeso! ')
elif 30 < imc <= 40:
    print(f'Seu IMC é {imc:.2f}, e seu status é Obesidade! ')
else:
    print(f'Seu IMC é {imc:.2f}, e seu status é Obesidade mórbida! ')
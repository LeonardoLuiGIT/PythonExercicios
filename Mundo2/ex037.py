""" Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
- 1 Para binário
- 2 Para octal
- 3 Para hexadecimal
"""

#Pede ao usuário a opção que ele quer e o número, se não for nenhuma das opções, ele gera um erro.
print('-=-'* 20)
print('CALCULADORA')
print('-=-' * 20)
while True:
    opcao = input('\n 1 para Binário'
                    '\n 2 para Octal'
                    '\n 3 para Hexadecimal'
                    '\n : ')

    if opcao in ['1', '2', '3',]:
        break
    else:
        print('❌ Opção inválida! Tente novamente.')
num = int(input('Digite o número: '))

if opcao == "1":
    num1 = bin(num)
    print('A opção escolhida foi Binário!')
    print(f'O número {num} em hexadecimal fica {num:b}')
elif opcao == "2":
    num1 = oct(num)
    print('A opção escolhida foi Octal!')
    print(f'O número {num} em hexadecimal fica {num:o}')
else:
    num1 = hex(num)
    print('A opção escolhida foi Hexadecimal!')
    print(f'O número {num} em hexadecimal fica {num:x}')

print('-=-'* 20)
print('CALCULADORA')
print('-=-' * 20)
while True:
    calculo = input('\n 1 para Adição'
                    '\n 2 para Subtração'
                    '\n 3 para Multiplicação'
                    '\n 4 para Divisão'
                    '\n : ')

    if calculo in ['1', '2', '3', '4']:
        break
    else:
        print('❌ Opção inválida! Tente novamente.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if calculo == "1":
    num3 = num1 + num2
    print('Resultado: {}'.format(num3))
elif calculo == "2":
    num3 = num1 - num2
    print('Resultado: {}'.format(num3))
elif calculo == "3":
    num3 = num1 * num2
    print('Resultado: {}'.format(num3))
elif calculo == "4":
    num3 = num1 / num2
    print('Resultado: {}'.format(num3))
print('FIM')
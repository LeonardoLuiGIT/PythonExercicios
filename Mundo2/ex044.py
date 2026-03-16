""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- Á vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão 20% de juros
"""

print("-=-" * 20)
print("Calcular valor de produto")
print("-=-" * 20)

prod = float(input('Preço das compras: R$'))

while True:
    pagmt = input('\n [ 1 ] à vista Dinheiro/Cheque'
                    '\n [ 2 ] Cartão de crédito'
                    '\n Qual é a opção?  ')

    if pagmt in ['1', '2']:
        break
    else:
        print('❌ Opção inválida! Tente novamente.')

if pagmt == '1':
    valor = prod - (prod * 0.10)
    print(f'A sua compra de R${prod:.2f}, vai custar R${valor:.2f} no final com 10% de desconto!')
else:
    parc = int(input('Quantidade de parcelas: '))
    if parc == 1:
            valor = prod - (prod * 0.05)
            parc2 = parc / prod
            print(f'Sua compra será parcelada em 1x de R${valor:.2f}!')
            print(f'Sua compra de R${prod:.2f} vai custar no final R${valor:.2f} com 5% de desconto!')
    elif parc == 2:
        parc2 = prod / 2
        print(f'Sua compra será parcelada em 2x de R${parc2:.2f} sem juros!')
        print(f'Sua compra de R${prod:.2f} vai custar no final R${prod:.2f}!')
    else:
        valor = prod + (prod * 0.20)
        parc2 = valor / parc
        print(f'Sua compra será parcelada em {parc}x de R${parc2:.2f} com juros!')
        print(f'Sua compra de R${prod:.2f} vai custar no final R${valor:.2f}!')
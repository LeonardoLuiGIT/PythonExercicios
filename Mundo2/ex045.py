""" Crie um programa que faça o computador jogar Jokenpô com você"""

import random
from time import sleep

print("-=-" * 20)
print("JOKENPÔ")
print("-=-" * 20)

while True:
    plyer = input('\n   Escolha uma opção para jogar!'
                  '\n [ Pedra ]'
                  '\n [ Papel ]'
                  '\n [ Tesoura ]'
                    '\n Sua jogada: ').lower().strip()

    if plyer in ['pedra', 'papel', 'tesoura']:
        break
    else:
        print('❌ Opção inválida! Tente novamente.')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

jogo = ['pedra', 'papel', 'tesoura']
pc = random.choice(jogo)

if plyer == pc:
    print('As duas jogadas, resultaram em um empate! 😳')
elif (plyer =='pedra' and pc == 'tesoura') or (plyer =='papel' and pc == 'pedra') or (plyer =='tesoura' and pc == 'papel'):
    print(f'Você ganhou, o PC jogou {pc}, PARABÉNS!! 😄 ')
else:
    print(f'Você infelizmente perdeu, o PC jogou {pc}! 😢 ')
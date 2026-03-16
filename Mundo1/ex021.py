import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Solicita entrada do utilizador
opcao = input("Digite 1 para Make You Fell Loved \n 2 para Aviva para tocar a música: ")

# Para qualquer música que esteja a tocar
pygame.mixer.music.stop()

if opcao == "1":
    pygame.mixer.music.load("../Musicas/ex021.mp3")  # Substitua pelo nome do seu arquivo
    pygame.mixer.music.play()
    print("Tocando música 1...")

elif opcao == "2":
    pygame.mixer.music.load("../Musicas/aviva.mp3")
    pygame.mixer.music.play()
    print("Tocando música 2...")

else:
    print("Música não encontrada.")

# Mantém o programa rodando enquanto a música toca
input("Pressione Enter para parar...")

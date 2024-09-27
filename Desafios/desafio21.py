# tocar uma musica em python

import pygame
# Inicializa o mixer
pygame.mixer.init()
# Carrega a música
pygame.mixer.music.load('AQUELAS COISAS - João Gomes e Tarcísio do Acordeon.mp3')
# Toca a música
pygame.mixer.music.play()



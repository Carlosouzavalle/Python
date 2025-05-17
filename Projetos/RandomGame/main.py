# imports nescessarios
import pygame
from pygame.locals import *
from sys import exit
from random import randint

#inicializa todas as funções
pygame.init()

# criação da tela do game
screen_height = 640
screen_whidth = 480
screen = pygame.display.set_mode((screen_height, screen_whidth))
# setando nome de exibição no topo do game
pygame.display.set_caption('Random Game')

# movimentação do objeto
x = screen_height/2
y = screen_whidth/2
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial',  30, True, True)
# tipo da fonte, tamanho da fonte, netrigo, italico 

# variaveis enemy
blue_x = randint(40, 600)
blue_y = randint(50, 430)

pontos = 0
print(pygame.font.get_fonts())

# todo codigo aqui dentro vai ficar em loop
while True:
    clock.tick(64)
    screen.fill((0,0,0))
    mensage = f'Pontos: {pontos}'
    formatedText = font.render(mensage, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # movimentando um objeto 
        """if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 10
            elif event.key == K_d:
                x = x + 10
            elif event.key == K_w:
                y = y - 10
            elif event.key == K_s:
                y = y + 10"""
     
    # uma movimentação um tanto diferente aqui movimentamos segurando a tecla           
    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    elif pygame.key.get_pressed()[K_d]:
        x = x + 10
    elif pygame.key.get_pressed()[K_w]:
        y = y - 10
    elif pygame.key.get_pressed()[K_s]:
        y = y + 10
    
    # desenhando objetos na tela        
    red_player = pygame.draw.rect(screen, (255,0,0), (x, y, 40, 50))
    blue_enemy = pygame.draw.rect(screen, (0,0,255), (blue_x, blue_y, 40, 50))
    
        
    if red_player.colliderect(blue_enemy):
        blue_x = randint(40, 600)
        blue_y = randint(50, 430)
        pontos = pontos +1
    
    screen.blit(formatedText, (450, 40))

    """
    pygame.draw.rect(screen, (255,0,0), (200, 300, 40, 50))
    
    1: parametros é a sua tela
    2: a cor do objeto a ser desenhado
    3: posição x
    4: posição y
    5: comprimento em px
    6: altura em px
    """
 
    pygame.display.update()
import pygame
from os.path import join
import random 

# general setup
pygame.init() 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True
clock = pygame.time.Clock()

surf = pygame.Surface((100, 200))
x = 100

# imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star = pygame.image.load(join('images', 'star.png')).convert_alpha()
meteor = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser = pygame.image.load(join('images', 'laser.png'))
player_direction = pygame.math.Vector2()


player_rect = player_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_rect = meteor.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_rect = laser.get_rect(bottomleft = (20, WINDOW_HEIGHT - 20))



# stars in background
posicoes = []
for _ in range(20):
    x = random.randint(0, WINDOW_WIDTH - 50)
    y = random.randint(0, WINDOW_HEIGHT - 50)
    posicoes.append((x, y))



# game loop
while running:
    clock.tick(24)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display_surface.fill('black')
    #x += 0.1
    
    #player movement
    player_rect.x += player_direction * 100
    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction *= -1
    
    display_surface.blit(player_surf,player_rect)
    display_surface.blit(meteor,meteor_rect)
    display_surface.blit(laser, laser_rect)
    
    
    for pos in posicoes:
        display_surface.blit(star, pos)
    
    pygame.display.update()
    
pygame.quit()
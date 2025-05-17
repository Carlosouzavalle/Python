import pygame


# general setup
pygame.init() 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True


surf = pygame.Surface((100, 200))
x = 100

# import an image
player_surf = pygame.image.load('images/player.png')


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display_surface.fill('gray')
    x += 0.1
    display_surface.blit(player_surf, (x,150))
    pygame.display.update()
    
pygame.quit()
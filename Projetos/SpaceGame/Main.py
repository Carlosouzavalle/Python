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


# imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star = pygame.image.load(join('images', 'star.png')).convert_alpha()
meteor = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser = pygame.image.load(join('images', 'laser.png'))


player_rect = player_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_rect = meteor.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_rect = laser.get_rect(bottomleft = (20, WINDOW_HEIGHT - 20))


# controle de personagem
x_player = WINDOW_WIDTH/2
y_player = WINDOW_HEIGHT/2


# atirar o laser
lasers = []
laser_cooldown = 500
last_laser_time = 0


# stars in background
posicoes = []
for _ in range(20):
    x = random.randint(0, WINDOW_WIDTH - 50)
    y = random.randint(0, WINDOW_HEIGHT - 50)
    posicoes.append((x, y))

meteors = []
spawn_delay = 500
last_spawn_time = pygame.time.get_ticks()

# variaveis para controle da imagem e colisão
player_visible = True
hit_timer = 0
cooldown = 1000

life = 10
font = pygame.font.SysFont('arial',  30, True, True)


# game loop
while running:
    #frame rate
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    display_surface.fill('black')
    
    # SPANW DINÂMICO DE METEOROS
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_delay:
        x = random.randint(0, WINDOW_WIDTH - meteor.get_width())
        y = random.randint(-100, -40)
        rect = meteor.get_rect(topleft=(x, y))
        meteors.append(rect)
        last_spawn_time = current_time
        
        
    # MOVIMENTAR E DESENHAR METEOROS
    for rect in meteors:
        rect.y += 200 * dt
        
        if rect.top > WINDOW_HEIGHT:
            meteors.remove(rect)
            continue
        display_surface.blit(meteor, rect)
        
        
        #collision
        if rect.colliderect(player_rect) and hit_timer <= 0:
            print("bateu")
            
            hit_timer = cooldown
            player_visible = False
            life -= 1
            

        # Timer de hit
        if hit_timer > 0:
            hit_timer -= dt * 1000  # Multiplica para ficar em milissegundos
            # Piscar
            if hit_timer % 300 < 150:
                player_visible = False
            else:
                player_visible = True
        else:
            player_visible = True
            
    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x_player -= 200 * dt
    if keys[pygame.K_d]:
        x_player += 200 * dt
    if keys[pygame.K_s]:
        y_player += 200 * dt
    if keys[pygame.K_w]:
        y_player -= 200 * dt
        

    if keys[pygame.K_SPACE] and current_time - last_laser_time > laser_cooldown:
        laser_x = player_rect.centerx - laser.get_width() // 2
        laser_y = player_rect.top
        laser_rect_new = laser.get_rect(topleft=(laser_x, laser_y))
        lasers.append(laser_rect_new)
        last_laser_time = current_time
        

    #atualiza para a nova posição
    player_rect.center = (x_player, y_player)
    
  
    # apresentando na tela
    if player_visible:
        display_surface.blit(player_surf,player_rect)

    display_surface.blit(laser, laser_rect)
    
    # esses blocos mostra o texto da vida não fico do jeito que eu queria mais vai assim
    life_text = f'Life: {life}'
    formatedText = font.render(life_text, True, (255, 255, 255))
    # o primeiro parametro é 'X' e o segundo é 'y'
    display_surface.blit(formatedText, (100, 30))
    
    
    for pos in posicoes:
        display_surface.blit(star, pos)
    
    for laser_rect in lasers[:]:  # Faz uma cópia da lista
        laser_rect.y -= 400 * dt  # velocidade do laser

        if laser_rect.bottom < 0:
            lasers.remove(laser_rect)
            continue
        
    for meteor_rect in meteors[:]:
        if laser_rect.colliderect(meteor_rect):
            meteors.remove(meteor_rect)
            if laser_rect in lasers:
                lasers.remove(laser_rect)
            break


        display_surface.blit(laser, laser_rect)
    
    
    pygame.display.update()
    
pygame.quit()
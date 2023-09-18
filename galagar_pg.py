import time
import pygame
from sys import exit
from random import randint
pygame.init()

# Game Surface ------------------------
#screen = 
pygame.display.set_mode ((400, 600))
pygame.display.set_caption ('GalaGar 2050')
clock = pygame.time.Clock()
# --------------------------------------

# Load Font
game_font = pygame.font.Font('fonts/arcade.ttf', 30)

# Load and declare title banner --------------------
title = game_font.render ('GalaGar 2050', False, 'Red')
title_rect = title.get_rect(center = (200, 30))
# ----------------------------

# Player --------------------------
player_surf = pygame.image.load ('images/bug.png').convert_alpha ()
player_rect = player_surf.get_rect(midbottom = (200,600))
#---------------------

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
        
    # Controls -------------------------------------
    keys = pygame.key.get_pressed()    
    if keys [pygame.K_LEFT]:
        if player_rect.x > -10:
            player_rect.x -= 5 
    if keys [pygame.K_RIGHT]:
        if player_rect.x < 330:
            player_rect.x += 5
    if keys [pygame.K_UP]:
        if player_rect.y > 450:
            player_rect.y -= 5
    if keys [pygame.K_DOWN]:
        if player_rect.y < 520:
            player_rect.y += 5            
    # ----------------------------------------------

    screen.fill((10, 10, 10))
    screen.blit (title, title_rect)
    screen.blit (player_surf, player_rect)
            
    pygame.display.update()
    clock.tick (60)
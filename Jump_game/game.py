import pygame
import game_fuctions as gf
import random
size = [800,800]
screen = pygame.display.set_mode(size)
bg = pygame.image.load("bg.jpg")
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
player = gf.Player(50, 400)
list_cubs_condition = False
cubs = []
k = 0
print(len(cubs))
last_obj = 12
first_obj = 0
#cub_1 = gf.Cubs(1)
active = True
clock = pygame.time.Clock()
while active:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    screen.blit(bg, (0, 0))
    player.draw(screen)
    player.movement()
    print(len(cubs))
    k = k + 1
    if list_cubs_condition == False:
        for i in range(first_obj, last_obj):
            cubs.append(gf.Cubs(900 + i * 150))
            list_cubs_condition = True

    
    for i in range(0, len(cubs)):
        if cubs[i].poz_x < -50:
            cubs[i].out_of_range = True
            print("deleted")
        if cubs[i].out_of_range == False:
            cubs[i].draw(screen)
            cubs[i].frame_moving()
    if len(cubs) == 0:
        list_cubs_condition = False
        first_obj = 0
        last_obj = 12
    if k >= len(cubs):
        k = 0
    if len(cubs) > 0:
        if cubs[k].out_of_range == True:
            del cubs[k]
            
    #cub_1.draw(screen)
    #if cub_1.collision(player.player_x, player.player_y):
     #   player.player_x = cub_1.poz_x - 40
   
    pygame.display.flip()
    
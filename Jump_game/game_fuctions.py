import pygame
import math
import random
BLACK = (0, 0, 0)

def Get_key():
    key_value = 0
    if pygame.key.get_pressed()[pygame.K_w]:
        key_value = 1
    elif pygame.key.get_pressed()[pygame.K_s]:
        key_value = 2
    elif pygame.key.get_pressed()[pygame.K_a]:
        key_value = 3
    elif pygame.key.get_pressed()[pygame.K_d]:
        key_value = 4
    return key_value
class Player:

    def __init__(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        self.width = 30
        self.height = 50
        self.angle = math.sqrt(2)/2
        self.image = pygame.image.load("player.png")
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, [self.player_x, self.player_y , self.width, self.height])
    def movement(self):
        if Get_key() == 1:
            self.player_y -= math.cos(self.angle) * 6
            #print(self.player_y) 
            #self.player_x += 3

        else:
            self.player_y += math.cos(self.angle) * 6
           # print(self.player_y)
            #self.player_x += 1
    
class Cubs:

    def __init__(self, poz_x):
        self.poz_x = poz_x
        self.poz_y = random.randrange(100, 700)
        self.width = random.randrange(30, 50)
        self.height = random.randrange(150, 200)
        self.out_of_range = False
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, ((self.poz_x, self.poz_y), (self.width, self.height)))

    def collision(self, player_x, player_y):
        if player_x + 25 > self.poz_x and player_x < self.poz_x + self.width and player_y + 25> self.poz_y and player_y < self.poz_y + self.height:
            return True
    def change(self, prev_x, prev_y):
        if self.poz_x + 200 > prev_x and self.poz_x - 200 < prev_x:
            return True
    def frame_moving(self):
        self.poz_x -= 5
    def frame_condition(self):
        if self.poz_x <= 0:
            return True

    
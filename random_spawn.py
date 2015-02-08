import pygame
import os
import random

img_path2 = os.path.join('C:\Python27\pyfiles', 'plate.png')


class Rock(object):
    def __init__(self, x=640, y=0, dist=10):
       self.image = pygame.image.load(img_path2)
       self.x = x
       self.y = y
       self.dist = dist
    def rock(self):
        dist = 10
        if running == True:
            self.x -=dist


    def rock_draw(self, surface):
        surface.blit(self.image, (self.x, self.y))






pygame.init()
screen = pygame.display.set_mode((640, 400))

rock = Rock()


clock = pygame.time.Clock()

running = True
while running:
    if rock.x < 0:
        y = random.randint(0, 400)
        rock = Rock(640, y)

    rock.rock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            running = False

    rock.rock()
    
    screen.fill((255,255,255)) 
    rock.rock_draw(screen)
    pygame.display.update() 

    clock.tick(40)

import pygame
from pygame.locals import *
from random import choice
#from mastermind import *
import time

pygame.init()
pygame.font.init()

width_master, height_master = 710, 240
width, height = 796, 550

# ---- Couleurs ----
GREEN = (0,210,0)
RED = (210,0,0)
BLUE = (0,0,210)
YELLOW = (210,210,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (130,130,130)

color = [YELLOW, BLUE, RED, GREEN]

pygame.display.set_caption('Mastermind')
screen = pygame.display.set_mode((width,height))
screen.fill(WHITE)

# ---- Surfaces ----
grille = pygame.Surface((width_master, height_master))
rect_grille = grille.get_rect()

def text_draw(text, position, color, size):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface,position)

def affiche():

    front_image = pygame.image.load('pictures/front.png').convert_alpha()
    front_image = pygame.transform.scale(front_image, (width, height))
    screen.blit(grille, (45,45,width_master,height_master))
    screen.blit(front_image, (0,0,width,height))
    pygame.display.update()

def fill_tab(x, color_fill):
    lenthx = width_master//12
    lenthy = height_master//4

    for y in range(4):
        pygame.draw.rect(grille, color_fill[y], (x*lenthx,y*lenthy,lenthx,lenthy))
    affiche()


#gen_tab()
affiche()
x = 0
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                fill_tab(x, (choice(color),choice(color),choice(color),choice(color)))
                x += 1
                if x == 12 :
                    pygame.quit()
                    quit()

import pygame
from pygame.locals import *
from random import choice
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

x = 0
y = 0
user = []
result = [0,0,0] #yes, no, maybe
yes = "0"
maybe = "0"

pygame.display.set_caption('Mastermind')
screen = pygame.display.set_mode((width,height))
screen.fill(WHITE)

# ---- Surfaces ----
grille = pygame.Surface((width_master, height_master))
rect_grille = grille.get_rect()

def soluce_def():
    soluce = []
    for i in range(4):
        soluce.append(choice(color))
    return soluce

soluce = soluce_def()

def text_draw(text, position, color, size):
    myfont = pygame.font.SysFont('Arial', size)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface,position)

def affiche():
    front_image = pygame.image.load('pictures/front.png').convert_alpha()
    front_image = pygame.transform.scale(front_image, (width, height))
    screen.blit(grille, (45,45,width_master,height_master))
    screen.blit(front_image, (0,0,width,height))
    return_result()
    pygame.display.update()

def fill_tab(x, y, color_fill):
    lenthx = width_master//12
    lenthy = height_master//4
    pygame.draw.rect(grille, color_fill, (x*lenthx,y*lenthy,lenthx,lenthy))
    affiche()

def fill_case(color):
    global y,x,user
    fill_tab(x, y, color)
    user.append(color)
    y += 1
    if y == 4 :
        check()
        y = 0
        x += 1

def end_game():
    win_image = pygame.image.load('pictures/perdu.png')
    win_image = pygame.transform.scale(win_image, (width, height))
    screen.blit(win_image, (0,0,width,height))
    pygame.display.update()

    # A delet
    time.sleep(2)
    pygame.quit()
    quit()

def win():
    win_image = pygame.image.load('pictures/win.png')
    win_image = pygame.transform.scale(win_image, (width, height))
    screen.blit(win_image, (0,0,width,height))
    pygame.display.update()

    # A delet
    time.sleep(2)
    pygame.quit()
    quit()

def return_result():
    global yes, maybe
    if y == 4:
        yes =  str(result[0])
        maybe = str(result[1])
    str_result_yes = "YES = " + yes
    text_draw(str_result_yes, (590,425), WHITE, 25)
    str_result_in = "IN = " + maybe
    text_draw(str_result_in, (590,450), WHITE, 25)
    pygame.display.update()

def check():
    #result = [0,0,0] #yes, maybe, no
    global user
    for i in range(4):
        if user[i] == soluce[i]: #Si bonne place
            result[0] += 1
        elif user[i] in soluce: #Si dans la solution
            result[1] += 1
        else : #Si pas dans la solution
            result[2] += 1

    if result[0] == 4: # Si on a tout bon
        win()
    else : #Sinon
        affiche()

    # Clean des listes
    user.clear()
    result.clear()
    for i in range(3):
        result.append(0)

def restart():
    global x,y,user,soluce,result
    grille.fill(BLACK)
    affiche()
    soluce = soluce_def() # Nouvelle solution
    user.clear()
    result.clear()
    for i in range(3):
        result.append(0)
    y = 0
    x = 0

affiche()
while x != 12 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE: # affiche la solution
                for y_space in range(4) :
                    fill_tab(x, y_space, soluce[y_space])
                x += 1
                y = 0

            if event.key == K_1 or event.key == K_KP1: # Bleu
                fill_case(BLUE)
            if event.key == K_2 or event.key == K_KP2: # Vert
                fill_case(GREEN)
            if event.key == K_3 or event.key == K_KP3: # Jaune
                fill_case(YELLOW)
            if event.key == K_4 or event.key == K_KP4: # Rouge
                fill_case(RED)

            if event.key == K_r: # Restart
                restart()

end_game()

import pygame
from pygame import draw
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
clock = pygame.time.Clock()

#settings
winName = "Mostafa's Movies"
size =width, height = 1280, 720  #tuple

hoverX = False;
hoverSquare = False;
hoverMinus = False;
hoverStates = [hoverX, hoverSquare, hoverMinus]

image = pygame.image.load("unknown.png")
pygame.display.set_icon(image)
root = pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption(winName)

running = True

while running:
    mousePos = pygame.mouse.get_pos()

    #border
    #border - right side
    for i in range(1,4):
        if mousePos[0] < width-(40*(i-1)) and mousePos[0] > width-(40*i) and mousePos[1] > 0 and mousePos[1] < 25:
            hoverStates[i-1] = True

        else:
            hoverStates[i-1] = False

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                running = False              

    root.fill((57, 237, 222))

    #border

    #border - background
    draw.rect(root, (40, 184, 153), (0,0, width, 25))

    #border - elements
    #elements - x
    if hoverStates[0]: 
        colourX = (255,255,255)
        colourXback = (242, 27, 27)
    else:
        colourX = (40, 184, 153)
        colourXback = (40, 184, 153)    

    #elements - square
    if hoverStates[1]:
        colourSquareBack = (65, 209, 178)
        colourSquare = (255,255,255)
    else:
        colourSquare = (125, 245, 219)
        colourSquareBack = (40, 184, 153) 
    
    #elements - minus
    if hoverStates[2]:
        colourMinusBack = (65, 209, 178)
        colourMinus = (255,255,255)
    else:
        colourMinus = (125, 245, 219)
        colourMinusBack = (40, 184, 153)
    
    #colours array
    bordercolours = [[colourX, colourXback], [colourSquare, colourSquareBack], [colourMinus, colourMinusBack]]

    for i in range(1,4):
        draw.rect(root, bordercolours[i-1][1], (width-(i*40),0, 40, 25))

    pygame.display.update()
    clock.tick(120)

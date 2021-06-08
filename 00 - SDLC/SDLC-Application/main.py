import pygame
from pygame import color
from pygame._sdl2 import Window
import reference
from pygame import draw
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
import math
import time
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def colorImage(image, r, g, b, colourArr):
    newImage = image.copy()
    imgArray = pygame.surfarray.pixels3d(newImage)
    for y in range(40):
        for x in range(25):
            if imgArray[y,x,0] == 255:
                imgArray[y,x,0] = r
                imgArray[y,x,1] = g
                imgArray[y,x,2] = b 
            
            elif imgArray[y,x,0] == 178:
                imgArray[y,x,0] = r-40
                imgArray[y,x,1] = g-40
                imgArray[y,x,2] = b-40
            else:
                for colour in range(len(colourArr)):
                    imgArray[y,x,colour] = colourArr[colour]

    return pygame.surfarray.make_surface(imgArray)

pygame.init()

#settings
winName = "Mostafa's Movies"
size = width, height = 1280, 745  #tuple
winPos = (100,100)

root = pygame.display.set_mode(size, pygame.NOFRAME)

window = Window.from_display_module()

hoverX = False;
hoverSquare = False;
hoverMinus = False;
hoverStates = [hoverX, hoverSquare, hoverMinus]

startingBorderXimage = pygame.image.load('X.png')
startingBorderSquareImage = pygame.image.load('Square.png')
startingBorderMinusImage = pygame.image.load('minus.png')

startingBorderXimage.convert_alpha()
startingBorderSquareImage.convert_alpha()
startingBorderMinusImage.convert_alpha()

borderXimage = startingBorderXimage.copy()
borderSquareImage = startingBorderSquareImage.copy()
borderMinusImage = startingBorderMinusImage.copy()

borderImages = [borderXimage, borderSquareImage, borderMinusImage]

image = pygame.image.load("unknown.png")
pygame.display.set_icon(image)
pygame.display.set_caption(winName)

running = True

window.position = winPos
oldPos = (0,0)
draggingWin = False

maximized = False

backImageCorn = pygame.image.load('corn.png')
backImageFilm = pygame.image.load('film.png')
backImageClack = pygame.image.load('clack.png')

backImages = [backImageCorn, backImageFilm, backImageClack]

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
                if hoverStates[0] == True:
                    running = False 

                if hoverStates[1] == True:
                    if not maximized:
                        size = width, height = (1920,1080)
                        root = pygame.display.set_mode(size, pygame.NOFRAME)
                        window.position = (0,0)
                        maximized = True
                    else:
                        maximized = False
                        size = width, height = (1280, 745)
                        root = pygame.display.set_mode(size, pygame.NOFRAME)
                        window.position = (100,100)
                
                if not maximized:
                    if draggingWin == False:
                        mousePos = pygame.mouse.get_pos()
                        if mousePos[0] > 0 and mousePos[0] < width-120 and mousePos[1] > 0 and mousePos[1] < 25:
                            draggingWin = True
                            oldPos = pygame.mouse.get_pos()
        
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if not maximized:
                    if draggingWin:
                        draggingWin = False
                        mousePos = pygame.mouse.get_pos()
                        winPos = (winPos[0] - oldPos[0] + mousePos[0], winPos[1] - oldPos[1] + mousePos[1])
                        window.position = winPos

        if event.type == MOUSEMOTION:
            if not maximized:
                if draggingWin:
                    mousePos = pygame.mouse.get_pos()
                    winPos = (winPos[0] - oldPos[0] + mousePos[0], winPos[1] - oldPos[1] + mousePos[1])
                    window.position = winPos
                    

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
        colourX = (125, 245, 219)
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
    borderColours = [[colourX, colourXback], [colourSquare, colourSquareBack], [colourMinus, colourMinusBack]]

    for i in range(1,4):
        draw.rect(root, borderColours[i-1][1], (width-(i*40),0, 40, 25))
        currBorderImage = colorImage(borderImages[i-1], borderColours[i-1][0][0],borderColours[i-1][0][1], borderColours[i-1][0][2], borderColours[i-1][1])
        root.blit(currBorderImage, (width-(i*40),0))

    #Main Display
    # This commented code adds the wave shape in the background (Too laggy as it isnt an image / shape)
    # for x in range(width):
    #     for y in range(int(height/10)+50):
    #         if y > (50*math.sin((1/200)*x)+50):
    #             draw.rect(root, (255,255,255), (x+1, y+400, 1, 1))
    
    # Background
    # Background - Rectangle Shape
    draw.rect(root, (255,255,255), (0, 5 * height/ 8, width, height))

    # Background - Images
    # Images - Popcorn
    backImages[0] = pygame.transform.scale(backImages[0], (300 * round(width/1280), 381 * round(height/720)))
    
    root.blit(backImages[0], (-(width/10),1 * height / 4))

    # Images - Movie Tape
    backImages[1] = pygame.transform.scale(backImages[1], (518 * round(width/1280), 768 * round(height/720)))
    
    root.blit(backImages[1], ((8 * width/10),(1 * height / 6)))

    # Images - Movie clacker
    backImages[2] = pygame.transform.scale(backImages[2], (132 * round(width/1280), 103 * round(height/720)))
    
    root.blit(backImages[2], ((0),(9 * height / 10)))

    # Refresh Display
    pygame.display.update()
    

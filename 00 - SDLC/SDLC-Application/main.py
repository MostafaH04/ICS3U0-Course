import pygame
from pygame import color
from pygame._sdl2 import Window
import reference
import infoScript as inf
import updateScript as upd
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
clock = pygame.time.Clock()
font = pygame.font.Font('AdobeCleanBold.otf', 70)
font2 = pygame.font.Font('AdobeCleanBold.otf', 20)

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

enterButtonColors = [[(15,54,225),(20,64,255)],[(26, 53, 173),(20, 55, 204)]]
enterButtonHover = False

maximized = False

backImage = pygame.image.load('back.png')

titleImage = pygame.image.load("title.png")

backLoaded = False

movieImages = []
for i in range(5):
    movieImages.append(pygame.image.load(f"{i+1}.png"))
print(movieImages)
firstThree = True
secondThree = False

mainPage = True
moviePage = False

sliderColours = [(15,54,225), (26, 53, 173)]
sliderHover = False

movieSlidingAnim1 = False
movieSlidingAnim2 = False
slidingFactor1 = 0

movieHover = [False, False, False]

data = reference.refer().get()
movieInfo = inf.showInfo(data).screen()
timeInfo = inf.showInfo(data).time()
print(movieInfo)
print(timeInfo)

selection = False
pickedMovie = None

timeSelection = False
timeHover = [False, False, False, False, False]

seatSelection = False

while running:
    mousePos = pygame.mouse.get_pos()

    #border
    #border - right side
    for i in range(1,4):
        if mousePos[0] < width-(40*(i-1)) and mousePos[0] > width-(40*i) and mousePos[1] > 0 and mousePos[1] < 25:
            hoverStates[i-1] = True

        else:
            hoverStates[i-1] = False    

    if mainPage == True and mousePos[0] > width/2-250 and mousePos[0] < width/2+250 and mousePos[1] > height/2 and mousePos[1] < height/2 +100:
        enterButtonHover = True
    else:
        enterButtonHover = False
    
    if moviePage == True:
        if selection == False:
            if firstThree == True:
                if movieSlidingAnim1 != True and mousePos[0] > (width - 130) and mousePos[0] < (width - 100) and mousePos[1] < int(1*height/4)+333 and mousePos[1] > int(1*height/4)+273:
                    sliderHover = True
                else:
                    sliderHover = False
            
            if secondThree == True:
                if movieSlidingAnim2 != True and mousePos[0] > 100 and mousePos[0] < 130 and mousePos[1] < int(1*height/4)+333 and mousePos[1] > int(1*height/4)+273:
                    sliderHover = True
                else:
                    sliderHover = False
            
            for i in range(1,4):
                if mousePos[0] > int(i * width/4 - 135) and mousePos[0] < int(i * width/4 + 135) and mousePos[1] > int(1*height/4 +100) and mousePos[1] < int(1*height/4 +505):
                    if (i-1) < 2:
                        movieHover[i-1] = True
                    else:
                        if firstThree:
                            movieHover[i-1] = True
                else:
                    movieHover[i-1] = False

        else:
            if timeSelection:
                for i in range(len(timeInfo)):
                    if mousePos[0] > int(width/2 - 60) and mousePos[0] < int(width/2 + 60) and mousePos[1] > int(height/2 - 115 + i*70) and mousePos[1] < int(height/2 - 65 + i*70):                  
                        timeHover[i] = True
                    else:
                        timeHover[i] = False         
            
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
                
                if enterButtonHover == True:
                    mainPage = False
                    moviePage = True

                if sliderHover == True:
                    if firstThree == True:
                        slidingFactor1 = 0
                        movieSlidingAnim1 = True
                    else:
                        slidingFactor1 = 0
                        movieSlidingAnim2 = True

                if selection and ((mousePos[0] > 0 and mousePos[0] < int(width/2 - 150)) or (mousePos[0] > int(width/2 + 150) and mousePos[0] < width) or (mousePos[1] > 25 and mousePos[1] < int(height/2-150)) or (mousePos[1] > int(height/2 + 150) and mousePos[1] < height)):
                    selection = False
                    timeSelection = False
                
                for i in range(len(movieHover)):
                    if movieHover[i]:
                        if firstThree:
                            print(movieInfo[i])
                            pickedMovie = i
                            movieHover[i] = False
                            timeSelection = True
                            selection = True
                        elif secondThree and i!= 2:
                            print(movieInfo[i+3])
                            pickedMovie = i+3
                            selection = True
                            timeSelection = True
                            movieHover[i] = False


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

    # Main Page
    if mainPage == True:
        # Main - Background - Images
        tempBackImage = pygame.transform.scale(backImage, (round(1920 * (width/1920)), round(1080 * (height/1080))))
        root.blit(tempBackImage, (0,0))

        # Title
        root.blit(titleImage, (width/2 - 250,0))

        # Button
        if enterButtonHover == True:
            i = 1
        else:
            i = 0
        buttonBackColors = enterButtonColors[i]
        draw.rect(root, buttonBackColors[0], (width/2-245, height/2+5, 500, 100), border_radius= 4)
        draw.rect(root, buttonBackColors[1], (width/2-250, height/2, 500, 100), border_radius= 4)    

        # Button - Text
        enterButtonText = font.render('ENTER', True, (255,255,255), buttonBackColors[1])
        enterButtonRect = enterButtonText.get_rect()
        enterButtonRect.center = (int(width/2), int(height/2)+50)
        root.blit(enterButtonText, enterButtonRect)

    # Movie Page
    elif moviePage == True:
        # Logo
        tempTitle = pygame.transform.scale(titleImage, (200, 200))
        root.blit(tempTitle, (0,-30))
        
        # Title
        titleText = font.render('MOVIES', True, (20,64,255), (57, 237, 222))
        titleTextRect = titleText.get_rect()
        titleTextRect.center = (int(width/2), 200)
        root.blit(titleText, titleTextRect)

        # Navigator
        
        # Sliding animation
        if movieSlidingAnim1:
            if slidingFactor1 > -(width):
                slidingFactor1 -= 50
            else:
                slidingFactor1 = 0
                firstThree = False
                secondThree = True
                movieSlidingAnim1 = False
        
        if movieSlidingAnim2:
            if slidingFactor1 < (width):
                slidingFactor1 += 50
            else:
                slidingFactor1 = 0
                secondThree = False
                firstThree = True
                movieSlidingAnim2 = False

        # Movies
        if firstThree == True:
            for i in range(3):
                currMovImg = pygame.transform.scale(movieImages[i], (270,405))
                root.blit(currMovImg, (int((i+1)*width/4 - 135 + slidingFactor1),int(1*height/4)+100))

            if movieSlidingAnim1 != True:
                for i in range(len(movieHover)):
                    if movieHover[i]:
                        hoverRect = pygame.Surface((270,405))
                        hoverRect.set_alpha(240)
                        hoverRect.fill((245,245,245))
                        root.blit(hoverRect, (int((i+1) * width/4 - 135 + slidingFactor1),int(1*height/4)+100))

                        currInfo = movieInfo[i]
                        lines = [f"Screen #: {i+1}", f"Name: {currInfo['name']}", f"Genre: {currInfo['genre']}", f"Seats #: {currInfo['seats']}", f"Time: {currInfo['time']}hrs"]
                            
                        for j in range(len(lines)):
                            movieText = font2.render(lines[j], True, (20,64,255))
                            movieTextRect = titleText.get_rect()
                            movieTextRect.center = (int((i+1) * width/4), int(1*height/4)+ 135 + 40*(j+1))
                            root.blit(movieText, movieTextRect)

        elif secondThree == True:
            for i in range(2):
                currMovImg = pygame.transform.scale(movieImages[i+3], (270,405))
                root.blit(currMovImg, (int((i+1) * width/4 - 135 + slidingFactor1),int(1*height/4)+100))

            if movieSlidingAnim2 != True:
                for i in range(len(movieHover)):
                    if i != 2:
                        if movieHover[i]:
                            hoverRect = pygame.Surface((270,405))
                            hoverRect.set_alpha(240)
                            hoverRect.fill((245,245,245))
                            root.blit(hoverRect, (int((i+1) * width/4 - 135 + slidingFactor1),int(1*height/4)+100))
                            
                            currInfo = movieInfo[i+3]
                            lines = [f"Screen #: {i+4}", f"Name: {currInfo['name']}", f"Genre: {currInfo['genre']}", f"Seats #: {currInfo['seats']}", f"Time: {currInfo['time']}hrs"]
                                
                            for j in range(len(lines)):
                                movieText = font2.render(lines[j], True, (20,64,255))
                                movieTextRect = titleText.get_rect()
                                movieTextRect.center = (int((i+1) * width/4), int(1*height/4)+ 135 + 40*(j+1))
                                root.blit(movieText, movieTextRect)

                    
        # Slider
        if sliderHover:
            sliderColor = sliderColours[0]
        else:
            sliderColor = sliderColours[1]

        if firstThree == True:
            draw.polygon(root, sliderColor, [(width - 100, int(1*height/4)+303), (width-130, int(1*height/4)+333), (width-130, int(1*height/4)+273)])
        else:
            draw.polygon(root, sliderColor, [(100, int(1*height/4)+303), (130, int(1*height/4)+333), (130, int(1*height/4)+273)])
    
        # selection background
        if selection:
            select = pygame.Surface((width,height))
            select.set_alpha(200)
            select.fill((235,235,235))
            root.blit(select, (0, 25))
            draw.rect(root, (255,255,255), (int(width/2 - 250), int(height/2 - 250), 500, 500), border_radius= 10)
        
            # time selection
            if timeSelection:
                timeTitleText = font.render('Times', True, (20,64,255))
                timeTitleTextRect = timeTitleText.get_rect()
                timeTitleTextRect.center = (int(width/2), int(height/2 - 180))
                root.blit(timeTitleText, timeTitleTextRect)

                for i in range(len(timeInfo)):
                    if timeHover[i] == True:
                        timeBorderColor = (210, 210, 210)
                    else:
                        timeBorderColor = (235, 235, 235)

                    draw.rect(root, timeBorderColor, (int(width/2 - 60), int(height/2 - 115 + i*70), 120, 50), border_radius= 25)
                    timeText = font2.render(timeInfo[i], True, (0,0,0))
                    timeRect = timeText.get_rect()
                    timeRect.center = (int(width/2), int(height/2 - 90 + (i*70)))
                    root.blit(timeText, timeRect)

            # Seat selection

            # Sign In

            # Ticket Output


    # Refresh Display
    pygame.display.update()
    clock.tick(1000)
    

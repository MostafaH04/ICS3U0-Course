import pygame # importing the pygame library
from pygame import color # importing the colour class in the pygame library
from pygame._sdl2 import Window # importing the window class form the pygame library (allows me to move the window using the custom border made for the program)
import reference # imports the reference file in this directory 
import infoScript as inf # imports the infoScript file in this directory
import updateScript as upd # imports the updateScript File in this directory
from pygame import draw # imports the draw class from the pygame library
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION # imports some mouse constants from the pygame library for events (makes it easier when writing syntax to keep track of when the user presses a key)
import math # imports the math library (used for trig functions)
import time # imports the time library
from pygame.locals import ( # Imports from names for key events that I will be using later on (makes it easier whne writing the syntax)
    KEYDOWN,
    QUIT,
)

# Pygame does not allow you to change the colour of images, so I created a function that accesses an Image and changes the white to a specifc colour (specifically for pictures that I added)
# Mainly used when the mouse is hovering over the buttons on the border (or the x, minus, and square png files in this directory)
def colourImage(image, r, g, b, colourArr): 
    # And image is essentially an array, so I am using the .copy() method to copy the images cntent to a new Image that I will be working on (in order to not ruin the orginal image)
    newImage = image.copy()
    # To retrieve the array of a pygame formated image (image opened using pygame library methods) we use the .surfarray.pixels3d(imageName) method to get the array that has the rgb (red, green, blue) infromation of each pixel
    imgArray = pygame.surfarray.pixels3d(newImage)
    for y in range(40): # the image has 40 coloumns since they were normalized when created on photshop to 40 x 25
        for x in range(25): # Image has 25 rows (same reason for 40 coloumns ^)
            if imgArray[y,x,0] == 255: # checks if the colour of the pixel is white, and if yes sets to the selected r g b values given to the function as parameters
                imgArray[y,x,0] = r 
                imgArray[y,x,1] = g
                imgArray[y,x,2] = b 
            
            elif imgArray[y,x,0] == 178: # If the picture is another grey (grey used for square on photoshop) then it is also changed to the selected r g b values, but all are reduced by 40 to make them darker (as the grey was ment to be a shadow orginally)
                imgArray[y,x,0] = r-40
                imgArray[y,x,1] = g-40
                imgArray[y,x,2] = b-40
            else: # if its not white or grey, then its the background, so that is set to the values of the colourArr given to the function as a parameter, which sets it to the colour of the background
                for colour in range(len(colourArr)): # goes through the different colour values for the image and sets them to the required colour values to match the background
                    imgArray[y,x,colour] = colourArr[colour]

    return pygame.surfarray.make_surface(imgArray) # Since the image was converted to an array to be edited, it must be converted back to a pygame image using the .surfarray.make_surface(imgArray), which essentially turns the image into a pygame "surface" term used to specify graphical objects on the window (images, shapes, etc)


pygame.init() # Inializes the pygame library
font = pygame.font.Font('AdobeCleanBold.otf', 70) # sets the font to the adobe clean bold font in the directory (size 70)
font2 = pygame.font.Font('AdobeCleanBold.otf', 20) # sets the font to same font above, but size 20 (smaller text)

#settings
winName = "Mostafa's Movies" # the name for the window
size = width, height = 1280, 745  # the size information tuple stores info in this format: (width, height), which is helpful and reduces text when working with windows in pygame
winPos = (100,100) # tuble representing iniatial window positions

root = pygame.display.set_mode(size, pygame.NOFRAME) # Starts the display using the size tuple suggesting the initial width and height of the program, and the argument pygame.NOFRAME which asks the library to start the window for the application without a border (will be making my own custom border [colours look nicer :)])
window = Window.from_display_module() # calls in the window class imported from pygame, now setting this keyword window the function in window from_display_module, which makes it much easier to understand when writing and reading the syntax for moving the window around

hoverX = False; # Initial status for hovering the x button on the border (closes program)
hoverSquare = False; # Initial Status for hovering the square button on the border (maximize)
hoverMinus = False; # Initial Status for hovering the minus button on the border (minimize [does not work])
hoverStates = [hoverX, hoverSquare, hoverMinus]

startingBorderXimage = pygame.image.load('X.png') # Loads image for the x icon (on the border)
startingBorderSquareImage = pygame.image.load('Square.png') # Loads image for the square icon (on the border)
startingBorderMinusImage = pygame.image.load('minus.png') # Loads image for the minus icon (on the border)

startingBorderXimage.convert_alpha() #pygame intially loads images without the alpha variable (transperancy), this adds that to the image surface
startingBorderSquareImage.convert_alpha() # Same idea as previous line
startingBorderMinusImage.convert_alpha() # Same idea as previous 2 lines

borderXimage = startingBorderXimage.copy() # Copies the image contents over to a new variable (for the x icon)
borderSquareImage = startingBorderSquareImage.copy() # Same idea as above but for square
borderMinusImage = startingBorderMinusImage.copy() # Same idea as above but for minus

borderImages = [borderXimage, borderSquareImage, borderMinusImage] # Stores the different icons in array (to easily access them together)

window.position = winPos # sets the position of the window to the intial position set at winPos variable
oldPos = (100,100) # begins a variable called oldPos and is set to 0,0 (used for moving window)
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
pickedTime = None

seatSelection = False
totalSeatCalculated = False
pickedSeats = []
hoveredSeat = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
seatsSelected = len(pickedSeats)

seatContinue = False

signInPage = False
signInContinue = False
signUpHover = False
signUpPage = False

usernameDefault = 'Username'
passwordDefault = 'Password'
creditcardDefault = 'Credit Card'
emailDefault = 'email@email.com'

username = usernameDefault
password = passwordDefault
creditCard = creditcardDefault
email = emailDefault

userTyping = False
passTyping = False
cardTyping = False
emailTyping = False

def checkInfo(mode):
    global username
    global usernameDefault
    global password
    global passwordDefault
    infoList = [username, password]
    if mode == "signup":
        global creditCard
        global creditcardDefault
        global email
        global emailDefault
        
        if username == usernameDefault or password == passwordDefault or creditCard == creditcardDefault or email == emailDefault:
            return False
        else:
            return True
    
    elif mode == "signin":
        if username == usernameDefault or password == passwordDefault:
            return False
        else:
            return True  

ticketOut = False        

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
            
            if seatSelection:
                if mousePos[0] > int(width/2 + 90) and mousePos[0] < int(width/2 + 90 + 150) and mousePos[1] > int(height/2 + 190) and mousePos[1] < int(height/2 + 190 + 50):
                    seatContinue = True
                else:
                    seatContinue = False
            else:
                if mousePos[0] > int(width/2 + 90) and mousePos[0] < int(width/2 + 90 + 150) and mousePos[1] > int(height/2 + 190) and mousePos[1] < int(height/2 + 190 + 50):
                    signInContinue = True
                else:
                    signInContinue = False

                # (int(width/2 - 90), int(height/2 + 190) 150, 50
                if mousePos[0] > int(width/2 - 240) and mousePos[0] < int(width/2 - 90) and mousePos[1] > int(height/2 + 190) and mousePos[1] < int(height/2 + 240):
                    signUpHover = True
                else:
                    signUpHover = False
            
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if userTyping:
                    username = username[:-1]
                elif passTyping:
                    password = password[:-1]
                elif cardTyping:
                    creditCard = creditCard[:-1]
                elif emailTyping:
                    email = email[:-1]

            else:
                if userTyping:
                    username += event.unicode
                elif passTyping:
                    password += event.unicode
                elif cardTyping:
                    creditCard += event.unicode
                elif emailTyping:
                    email += event.unicode

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

                if selection and ((mousePos[0] > 0 and mousePos[0] < int(width/2 - 250)) or (mousePos[0] > int(width/2 + 250) and mousePos[0] < width) or (mousePos[1] > 25 and mousePos[1] < int(height/2-250)) or (mousePos[1] > int(height/2 + 250) and mousePos[1] < height)):
                    selection = False
                    timeSelection = False
                    seatSelection = False
                    totalSeatCalculated = False
                    signInPage = False
                    pickedSeats = []
                    username = usernameDefault
                    password = passwordDefault
                    creditCard = creditcardDefault
                    email = emailDefault
                    ticketOut = False
                
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

                for i in range(len(timeHover)):
                    if timeHover[i] == True:
                        pickedTime = timeInfo[i]
                        timeSelection = False
                        signInPage = False
                        seatSelection = True
                        timeHover[i] = False
                        totalSeatCalculated = False
                
                if seatSelection:
                    for y in range(len(hoveredSeat)):
                        for x in range(10):
                            if hoveredSeat[y][x] == 1:
                                if [y,x] in pickedSeats:
                                    pickedSeats.remove([y,x])
                                else:
                                    if seatsSelected < 11:
                                        pickedSeats.append([y,x])

                    seatsSelected = len(pickedSeats)

                if seatContinue and seatSelection and len(pickedSeats) > 0:
                    seatSelection = False
                    signInPage = True
                    seatContinue = False
                    username = usernameDefault
                    password = passwordDefault
                    creditCard = creditcardDefault
                    email = emailDefault

                if signInPage:
                    if signUpHover:
                        if signUpPage != True:
                            signUpPage = True
                            username = usernameDefault
                            password = passwordDefault
                            creditCard = creditcardDefault
                            email = emailDefault
                        elif checkInfo('signup'):
                            if upd.update().addUser(username, password, creditCard, email):
                                print("added")
                                signInPage = False
                                ticketOut = True
                            else:
                                print("already exists")
                    elif signInContinue:
                        if signUpPage:
                            signUpPage = False
                            emailTyping = False
                            cardTyping = False
                            username = usernameDefault
                            password = passwordDefault
                            creditCard = creditcardDefault
                            email = emailDefault
                        elif checkInfo('signin'):
                            if upd.update().checkUser(username, password):
                                print("Correct Info")
                                signInPage = False
                                signUpPage = False
                                ticketOut = True
                            else:
                                print("Try again")
                        print(checkInfo('signin'))

                    
                    if mousePos[0] > int(width/2 - 200) and mousePos[0] < int(width/2 +200):
                        if mousePos[1] > int(height/2 - 110) and mousePos[1] < int(height/2 - 65):
                            userTyping = True
                            username = ''
                        else:
                            userTyping = False
                        
                        if mousePos[1] > int(height/2 - 30) and mousePos[1] < int(height/2 + 15):
                            passTyping = True
                            password = ''
                        else:
                            passTyping = False
                        
                        if signUpPage:
                            if mousePos[1] > int(height/2 + 50) and mousePos[1] < int(height/2 + 95):
                                cardTyping = True
                                creditCard = ''
                            else:
                                cardTyping = False
                            
                            if mousePos[1] > int(height/2 + 130) and mousePos[1] < int(height/2 +175):
                                emailTyping = True
                                email = ''
                            else:
                                emailTyping = False
                                

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
        currBorderImage = colourImage(borderImages[i-1], borderColours[i-1][0][0],borderColours[i-1][0][1], borderColours[i-1][0][2], borderColours[i-1][1])
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
            if seatSelection:
                if totalSeatCalculated != True:
                    seatInfo = upd.update().seatInfo(pickedTime, pickedMovie)
                    allSeatInfo = seatInfo['all']['seats']
                    availableAllInfo = seatInfo['all']['available']
                    disableSeatInfo = seatInfo['disablity']['seats']
                    availableDisableInfo = seatInfo['disablity']['available']
                    totalSeatCalculated = True

                priceText = font2.render(f"Price: {seatsSelected * 10} CAD", True, (0,0,0))
                root.blit(priceText, (int(width/2 - 240), int(height/2 + 220)))

                if seatContinue:
                    colourCont = (3, 86, 252)
                    colourText = (255,255,255)
                else:
                    colourCont = (255,255,255)
                    colourText = (3, 86, 252)
                draw.rect(root, colourCont, (int(width/2 + 90), int(height/2 + 190), 150, 50), border_radius= 30)

                priceText = font2.render(f"Continue >", True, colourText)
                root.blit(priceText, (int(width/2 + 120), int(height/2 + 200)))

                seatStartingX = int(width/2 - 220)
                seatStartingY = int(height/2 - 230)
                for coloumns in range(8):
                    # non-disablity seats
                    for seat in range(allSeatInfo[coloumns]):
                        if availableAllInfo[seat][coloumns] == "True":
                            if (mousePos[0] > seatStartingX + (coloumns * 60) and mousePos[0] < seatStartingX + (coloumns * 60) + 25 and mousePos[1] > seatStartingY + (seat * 40) and mousePos[1] < seatStartingY + (seat * 40) + 25):
                                 seatColour = (50,50,50)
                                 hoveredSeat[coloumns][seat] = 1
                                 print(seat,coloumns)
                            else:
                                seatColour = (20,64,255)
                                hoveredSeat[coloumns][seat] = 0
                            if ([coloumns,seat] in pickedSeats):
                                seatColour = (50,50,50)
                        else:
                            seatColour = (255,0,0)
                        
                        draw.rect(root, seatColour, (seatStartingX + (coloumns * 60), seatStartingY + (seat * 40), 25,25), border_radius= 2)
                    # disability seats
                    for seat in range(allSeatInfo[coloumns], allSeatInfo[coloumns]+disableSeatInfo[coloumns]):
                        
                        if availableDisableInfo[seat-allSeatInfo[coloumns]][coloumns] == "True":
                            if (mousePos[0] > seatStartingX + (coloumns * 60) and mousePos[0] < seatStartingX + (coloumns * 60) + 25 and mousePos[1] > seatStartingY + (seat * 40) and mousePos[1] < seatStartingY + (seat * 40) + 25):
                                 seatColour = (50,50,50)
                                 hoveredSeat[coloumns][seat] = 1
                                 print(seat,coloumns)
                            else:
                                seatColour = (255,64,255)
                                hoveredSeat[coloumns][seat] = 0
                            if ([coloumns,seat] in pickedSeats):
                                seatColour = (50,50,50)
                        else:
                            seatColour = (255,0,0)

                        draw.rect(root, seatColour, (seatStartingX + (coloumns * 60), seatStartingY + (seat * 40), 25,25), border_radius= 2)


            # Sign In
            if signInPage:
                if signInContinue:
                    colourSignIn = (3, 86, 252)
                    colourSignInText = (255,255,255)
                else:
                    colourSignIn = (255,255,255)
                    colourSignInText = (3, 86, 252)
                draw.rect(root, colourSignIn, (int(width/2 + 90), int(height/2 + 190), 150, 50), border_radius= 30)

                priceText = font2.render(f"Sign In >", True, colourSignInText)
                root.blit(priceText, (int(width/2 + 130), int(height/2 + 200)))

                if signUpHover:
                    colourSignUp = (3, 86, 252)
                    colourSignUpText = (255,255,255)
                else:
                    colourSignUp = (255,255,255)
                    colourSignUpText = (3, 86, 252)
                draw.rect(root, colourSignUp, (int(width/2 - 240), int(height/2 + 190), 150, 50), border_radius= 30)

                priceText = font2.render(f"< Sign Up", True, colourSignUpText)
                root.blit(priceText, (int(width/2 - 210), int(height/2 + 200)))

                if signUpPage:
                    pageTitleText = font.render('Sign Up', True, (20,64,255))

                    # Credit Card
                    draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 + 50), 400, 45))
                    creditText = font2.render(creditCard, True, (20,64,255))
                    root.blit(creditText, (int(width/2 - 190), int(height/2 + 60)))

                    # Email
                    draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 + 130), 400, 45))
                    emailText = font2.render(email, True, (20,64,255))
                    root.blit(emailText, (int(width/2 - 190), int(height/2 + 140)))
                else:
                    pageTitleText = font.render('Sign In', True, (20,64,255))

                # Username
                draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 - 110), 400, 45))
                userText = font2.render(username, True, (20,64,255))
                root.blit(userText, (int(width/2 - 190), int(height/2 - 100)))

                # Password
                draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 - 30), 400, 45))
                passText = font2.render(password, True, (20,64,255))
                root.blit(passText, (int(width/2 - 190), int(height/2 - 20)))
                
                pageTitleRect = pageTitleText.get_rect()
                pageTitleRect.center = (int(width/2), int(height/2 - 180))
                root.blit(pageTitleText, pageTitleRect)

            # Ticket Output
            if ticketOut:
                pageTitleText = font.render('Reciept', True, (20,64,255))
                nameText = font2.render(f"Name: {username}", True, (20,64,255))
                costText = font2.render(f"Price: {seatsSelected * 10} CAD", True, (20,64,255))
                timeText = font2.render(f"Time: {pickedTime}", True, (20,64,255))
                screenText = font2.render(f"Screen: {pickedMovie+1}; {movieInfo[pickedMovie]['name']}", True, (20,64,255))
                seatTitleText = font2.render("Seats Picked:", True, (20,64,255))

                textArr = [nameText, costText, timeText, screenText, seatTitleText]

                for text in range(len(textArr)):
                    root.blit(textArr[text], (int(width/2 - 110), int(height/2 - 120 + 30 * text)))

                for seats in range(len(pickedSeats)):
                    row = pickedSeats[seats][1] + 1
                    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    coloumn = pickedSeats[seats][0]
                    seatText = font2.render(f"Seat {seats+1}: {alph[coloumn]}{row}", True, (0,0,0))
                    root.blit(seatText, (int(width/2 - 80), int(height/2 + 30 + 20 * seats)))
                print(pickedSeats)

                pageTitleRect = pageTitleText.get_rect()
                pageTitleRect.center = (int(width/2), int(height/2 - 180))
                root.blit(pageTitleText, pageTitleRect)

    # Refresh Display
    pygame.display.update()
    

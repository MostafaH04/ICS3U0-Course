############################################
#                                          #
#  Name: Mostafa Hussein                   #
#  Student Number: 899733                  #
#  Cohort: C                               #
#  Teacher: Mr. Ghorvei                    #
#  Class: ICS3U0                           #
#  Assignment: Movie Theatre Ordering      #
#  Due Date: June 22nd 2021                #
#                                          #
############################################


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
oldPos = (0,0) # begins a variable called oldPos and is set to 0,0 (used for moving window)
draggingWin = False # initiates boolean that represents if the window is being dragged
maximized = False # Iniates boolean that represents if the window is maximized

enterButtonColors = [[(15,54,225),(20,64,255)],[(26, 53, 173),(20, 55, 204)]] # array that repersents shadow and foreground colours for the enter button on enter page when hovered and not hovered
enterButtonHover = False # initiates a boolean that represents if the enterButton is beign hovered or not

backImage = pygame.image.load('back.png') #Loads the background image for the enter page (in 1080p)

titleImage = pygame.image.load("title.png") # Loads the Image for the logo of the movie theatre

movieImages = [] # Initiates an array that will be used to store the different movie images to be displayed
# goes through numbers 1 to 5 to load the images labeld 1.png till 5.png
for i in range(1,6):
    movieImages.append(pygame.image.load(f"{i}.png"))
# The movie page displays 3 movies at a time max, following booleans represent which 3 are displayed
firstThree = True # Sets the first three to be displayed
secondThree = False # Sets the second three to be displayed

mainPage = True # Iniates boolean for main page (starts true because main page starts first [with enter button])
moviePage = False # Initiates boolean for movie page (starts false, on after user presses enter to display movies)

sliderColours = [(15,54,225), (26, 53, 173)] # Array that represents the hover and non hover colours for the arrow that slide the movies to the right and left on movie page
sliderHover = False # Initiates the hover status of the slider buttons to false

movieSlidingAnim1 = False # Initiates boolean for the status of the animation for the first 3 movies
movieSlidingAnim2 = False # Initiates boolean for the status of the animation for the second 3 movies (only 2)
slidingFactor1 = 0 # The variable used to move the movies during the animations

movieHover = [False, False, False] # Boolean Array with each element representing which movie is hovered on the screen (3 becuase their is a max of 3 movies displayed on the screen)

data = reference.refer().get() # using the reference script in the directory this gets the reference to the data base, and uses the .get() method in the firebase_admin library to get the information in the database as a set and stores it in data
movieInfo = inf.showInfo(data).screen() # uses the showInfo class in the infoScript file in the directory to retrieve information about the possible screens (movies) using the data retrieved from the database
timeInfo = inf.showInfo(data).time() # uses the showInfo class in the inforScript file in the directory to retrieve information about the show times using the data retrieved from the database

selection = False # Boolean variable used to denote if the user is currently picking a movie (basically when the frame for choosing a movie and entering information pops up)
pickedMovie = None # Empty variable that will be used to store the movie that is picked by the user

timeSelection = False # Boolean Varaible used to denote if the user is picking the time for the movie (used to know which step of selection the user is on)
timeHover = [False, False, False, False, False] # Boolean array used to represent which time is being hovered (used to know which time the user is currently over)
pickedTime = None # Empty variable that will be used to store the the index of the time picked in the timeInfo array (the one retrieved from the database information)

seatSelection = False # Boolean variable used to denote if the user is currently picking their seat for the movie (used to know which step of the selection the user is on, if this is true, the user is picking their seats)
totalSeatCalculated = False # Boolean variable used to denote if the information about the seats at a screen, this is used in order to constantly update the status of the seats after the user opens the program, rather than once only when opening hte program (in the case that another user picks that seat )
pickedSeats = [] # Empty array/ list used to store the seats that are selected by the user (as the user picks something it is added[appended] else if they click it again or exit out, it is removed or [popped])
hoveredSeat = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
] # 2D 10 x 8 Array used to denote the seats are hoverd in a screen (this represents the maximum possible screen size such that it is compatitable for all the screens)
seatsSelected = 0 # Empty variable [int type] used to represent the number of seats selected (used to keep track, and make sure it isnt over 10)

seatContinue = False # Boolean variable used to denote if the continue button in the seat tab is hovered or not

signInPage = False # Boolean variable used to denote if the user is currently on the sign in page of the selection process
signInContinue = False # Boolean variable used to denote if the user is hovering the sign in button in the sign in / sign up page
signUpHover = False # Boolean variable used to denote if the user is hovering the sign up button in the sign in/ sign up page
signUpPage = False # Boolean variable used to denote if the user is currently on the sign up page of teh selection process

usernameDefault = 'Username' # String variable that stores the default value for the username (returns to this state if the user exits out) - Used in both sign up and sign in pages
passwordDefault = 'Password' # String variable that stores the default value for the password (returns to this state if the user exits out) - Used in both sign up and sign in pages
creditcardDefault = 'Credit Card' # String variable that stores the default value for the credit card (returns to this state if the user exits out) - Used only in sign up
emailDefault = 'email@email.com' # String variable that stores the default value for the email (returns to this state if the user exits out) - Used only in sign up

username = usernameDefault # Variable used to store users username on sign up and sign in (set to the default username variable at the start)
password = passwordDefault # Variable used to store users password on sign up and sign in (set to the default password variable at the start)
creditCard = creditcardDefault # Variable used to store users creditCard on sign up (set to the default credit cardvariable at the start)
email = emailDefault # Variable used to store users username on sign up(set to the default email variable at the start)

userTyping = False # Boolean set to denote if the user is currently typing in the username feild (during sign in and sign up)
passTyping = False # Boolean set to denote if the user is currently typing in the password feild (during sign in and sign up)
cardTyping = False # Boolean set to denote if the user is currently typing in the credit card feild (during sign in)
emailTyping = False # Boolean set to denote if the user is currentyl typing in the email feild (during sign up)

def checkInfo(mode): # Function used to check if the user info currently placed in the fields for sign up and sign in are not equal to the default ones (makes sure the user actually changed the info before trying to compare it with the database or add new info to the database) 
    # The mode argument for the function retrieves if the mode the user is using the function in (are they signing up or signing in) which helps to know which variables to compare
    global username # retrieves the global username variable since functions usually have local vairabls, and in order to access varaibles outside the function they are required to be global
    global usernameDefault # retrieves the global username default variable
    global password # retrieves the global passwrod variable
    global passwordDefault # retrieves the global password default variable
    if mode == "signup": # if the mode is actually signing up
        global creditCard # the function also then retrieves the global credit card variable
        global creditcardDefault # retrieves the global credit card default variable
        global email # retrieves the global email variable
        global emailDefault # retrieves the global email default variable
        
        if username == usernameDefault or password == passwordDefault or creditCard == creditcardDefault or email == emailDefault: # checks if any of the user's sign up info has still not been changed
            return False # if any feild has not been changed it returns back to the place the function was called False [indicating that some field have not been changed]
        
        elif "@" not in email or "." not in email: # checks to make sure that @ and . are in the email inputed which are the two main parts of an email
            return False # if they arent, false is returned to denote that something is inputed in the wrong format

        else:
            return True # if all the fields have changed, then it returns back to the place the function was called True [indicating that all the feilds were changed as wanted]
    
    elif mode == "signin": # if the function is actually called using the sign in mode it does not require the global variables for credit card info, or email
        if username == usernameDefault or password == passwordDefault: # checks if the users username and password fields where actually edited
            return False # if any of them were not, then it returns False [indicating that some field has not been changed]
        else:
            return True  # if all of them were edited, then it returns True [indicating taht all the fields were changed]

ticketOut = False  # Boolean to denote if the user is on the ticket out phase in selection (the transaction is complete and views the reciept / ticket)      

running = True # Boolean to denote that the program should keep running

while running:
    mousePos = pygame.mouse.get_pos() # retrieves the mouse position on the window that is stored in the pygame library (retrieved as a tuple such as: (x, y) and can be access like this for example: x = mousePos[0] [similar to arrays])

    #border 
    #border - right side
    for i in range(1,4): # loops through numbers 1 to 3 used to check if any of the border buttons are hovered
        if mousePos[0] < width-(40*(i-1)) and mousePos[0] > width-(40*i) and mousePos[1] > 0 and mousePos[1] < 25: # this checks if the mouse position is over one of the buttons (i represents which botton it is)
            hoverStates[i-1] = True # If the button number I is hovered then its state in the hoverStates boolean list is turned to True (i-1 is used, becuase lists and arrays in python count starting 0 not 1)

        else:
            hoverStates[i-1] = False # If the button number I is not hovered then its state in the hoverStates boolean list is turned to False if it isnt already (i-1 is used, becuase lists and arrays in python count starting 0 not 1)    

    #Main page
    #Enter button
    if mainPage == True and mousePos[0] > width/2-250 and mousePos[0] < width/2+250 and mousePos[1] > height/2 and mousePos[1] < height/2 +100: # checks if the mouse is over the enter button
        enterButtonHover = True # if it is then the enterButtonHover variable is set to True to denote that
    else:
        enterButtonHover = False # if the button is not hovered, it is set to False
    
    #Movie selection Page
    if moviePage == True:
        # If the user is currently NOT selecting specifics (time, seat, account, etc.)
        if selection == False:
            if firstThree == True: # If it is the first three movies currently displayed
                # Checks that hte sliding animation is not occuring, then checks if the user is over the page switch button (or the sliding button)
                if movieSlidingAnim1 != True and mousePos[0] > (width - 130) and mousePos[0] < (width - 100) and mousePos[1] < int(1*height/4)+333 and mousePos[1] > int(1*height/4)+273:
                    sliderHover = True # if the user is over that button, and the movies are currently not sliding, the hover status is set to true
                else:
                    sliderHover = False # if the user is NOT over the button, or the movies are currently sliding, then the hover status is set to False
            
            if secondThree == True: # If it is actually the second page or second three movies that are displayed, it does the same as above just for these specific movies
                if movieSlidingAnim2 != True and mousePos[0] > 100 and mousePos[0] < 130 and mousePos[1] < int(1*height/4)+333 and mousePos[1] > int(1*height/4)+273:
                    sliderHover = True
                else:
                    sliderHover = False
            
            for i in range(1,4): # Loops through numbers 1 to 3 to check if the mouse is hovering on one of the three movies on the screen
                if mousePos[0] > int(i * width/4 - 135) and mousePos[0] < int(i * width/4 + 135) and mousePos[1] > int(1*height/4 +100) and mousePos[1] < int(1*height/4 +505): # If the mouse is over the current movie (i)
                    if (i-1) < 2: # if the current movie is currently hovered and is the first or second movie
                        movieHover[i-1] = True # set the movieHover status boolean in the boolean array for that movie to true
                    else: # if its the 3 rd movie that is being hovered
                        if firstThree: # check if the moive is in the first three (if its not that means its the second three and their is not third movie [we are using 5 movies])
                            movieHover[i-1] = True # sets the hover state for the 3rd movie to True
                else: # if the current movie is not being hovered
                    movieHover[i-1] = False # set its hover state to False

        else: # If the user is currently instead selecting specifics like the time, seat and more (after picking the movie)
            if timeSelection: # Checks if the user is currently selecting the time they want to attend
                for i in range(len(timeInfo)): # Loops through the different times in the timeInfo list
                    if mousePos[0] > int(width/2 - 60) and mousePos[0] < int(width/2 + 60) and mousePos[1] > int(height/2 - 115 + i*70) and mousePos[1] < int(height/2 - 65 + i*70): # Chceks if the user is currently hovering over one of the times               
                        timeHover[i] = True # if they are, the position relative to the time they are hovering is set to True in the boolean list for the times hovered
                    else:
                        timeHover[i] = False # if the current time is not hovered, then its status is set to False
            
            elif seatSelection: # Checks if the user is currently selecting their seat instead
                if mousePos[0] > int(width/2 + 90) and mousePos[0] < int(width/2 + 90 + 150) and mousePos[1] > int(height/2 + 190) and mousePos[1] < int(height/2 + 190 + 50): # checks if the user is hovering the continue button on that page
                    seatContinue = True # if they are it, the hover boolean for it is set to True
                else:
                    seatContinue = False # if not, the hover boolean is set to false
            else: # if the user is not selecting their seat, then they are on the sign in and sign up pages
                if mousePos[0] > int(width/2 + 90) and mousePos[0] < int(width/2 + 90 + 150) and mousePos[1] > int(height/2 + 190) and mousePos[1] < int(height/2 + 190 + 50): # checks if the user is hovering the sign in button
                    signInContinue = True # if they are, the sign in hover boolean is set to true
                else:
                    signInContinue = False # else the sign in hover boolean is set to false

                # Sign up button hover
                if mousePos[0] > int(width/2 - 240) and mousePos[0] < int(width/2 - 90) and mousePos[1] > int(height/2 + 190) and mousePos[1] < int(height/2 + 240): # checks if the user is hovering over the sign up button
                    signUpHover = True # if they are, the sign up hover boolean is set to true
                else:
                    signUpHover = False # else it is set to false
            
    for event in pygame.event.get(): # retrieves all the "events" that are captured by pygame (this mainly includes mouse and keyboard inputs)
        if event.type == pygame.KEYDOWN: # checks the events if it was a key pressed down (using the .type method (from pygame))
            if event.key == pygame.K_BACKSPACE: # if the key pressed is specifically backspace (pygame.K_BACKSPACE represents backspace in the pygame library)
                if userTyping: #checks if the user is typing the username
                    username = username[:-1] # if they are, then remove the last character
                elif passTyping: # checks if the user is typing their password
                    password = password[:-1] # if they are then remove the last character
                elif cardTyping: # checks if the user is typing their credit card info
                    creditCard = creditCard[:-1] # if they are then remove the last character
                elif emailTyping: # checks if the user is typing their email
                    email = email[:-1] # if they are then remove the last character

            else: # if the key was not a backsapce (it types it instead)
                if userTyping: # checks if the user is typing their username
                    username += event.unicode # adds the character to the end of the string
                elif passTyping: # checks if the user is typing their password
                    password += event.unicode # if they are, it adds a character to the end of the string
                elif cardTyping: # checks if the user is typing their credit card info
                    if event.unicode in "0123456789": # checks if the key pressed is a number
                        creditCard += event.unicode # if they are, then it adds the number to the end of the string
                elif emailTyping: # checks if the user is typing their email
                    email += event.unicode # if they are, it adds the character to the end of the string

        if event.type == MOUSEBUTTONDOWN: # checks the event if it was a button pressed down
            if event.button == 1: # checks if the button presses in button 1 (denotes left click)
                if hoverStates[0] == True: # if a click occurs and the user is hovering the x button on the border
                    running = False # terminates the program

                if hoverStates[1] == True: # if a click occurs and the user is hovering the square on the border
                    if not maximized: # checks if the screen is not maximized
                        size = width, height = (1920,1080) # sets a new width and height for the screen (1920 * 1080 [1080p])
                        root = pygame.display.set_mode(size, pygame.NOFRAME) #uses the size to reset the window for the program
                        window.position = (0,0) # sets the window position to 0, 0 on the monitor
                        maximized = True # sets the boolean that denotes if the window is maximized to True
                    else: # if the screen was already maximized
                        maximized = False # sets maximized to false
                        size = width, height = (1280, 745) # sets the width and height to a new size
                        root = pygame.display.set_mode(size, pygame.NOFRAME) # uses the size to reset teh window for the program
                        window.position = (100,100) # sets the window position to 100, 100 on the monitor
                
                if enterButtonHover == True: # if the user clicks and they are hovering the enter button on the main page
                    mainPage = False # the boolean denoting the main page is on is set to false
                    moviePage = True # the boolean denoting the movie page is set to True
                    # basically switches to the movie page

                if sliderHover == True: # if the user clicks and they are overing the slider buttons
                    if firstThree == True: # if the user is currently on the first three movies
                        slidingFactor1 = 0 # resets the sliding factor
                        movieSlidingAnim1 = True # then sets the boolean denoting the sliding animation for the first page to True
                    else: # if the user is instead on the second three movies
                        slidingFactor1 = 0 # resets the sliding factor again
                        movieSlidingAnim2 = True # sets the boolean denoting the sliding animation for second page to True
                
                # checks if the user is on the selection page and mouse is clicked on the edges of the screen (off the selection window)
                if selection and ((mousePos[0] > 0 and mousePos[0] < int(width/2 - 250)) or (mousePos[0] > int(width/2 + 250) and mousePos[0] < width) or (mousePos[1] > 25 and mousePos[1] < int(height/2-250)) or (mousePos[1] > int(height/2 + 250) and mousePos[1] < height)):
                    # if that is the case then it closes the window (returns to movie page basically)
                    selection = False # sets boolean denoting selection is on to false
                    timeSelection = False # sets boolean denoting that the user is currently selecting the time to false
                    seatSelection = False # sets teh boolean denoting that hte user is currently selecting their seat to false
                    totalSeatCalculated = False # sets the boolean denoting that the seat information has been retrieved to false
                    signInPage = False # sets the boolean denoting that the user is on the sign in page to false
                    pickedSeats = [] # resets the picked seats array
                    username = usernameDefault # resets the username string 
                    password = passwordDefault # resets the password string
                    creditCard = creditcardDefault # resets the credit card info string
                    email = emailDefault # resets the email string
                    ticketOut = False # sets the boolean denoting that the user is currently viewing their reciept / ticket to false
                
                for i in range(len(movieHover)): # goes through numbers 0 to 2 (denoting the 3 movies that could be hovered)
                    if movieHover[i]: # if the current movie hover boolean is true and its clicked
                        if firstThree: # checks if its currently the first 3 movies on
                            pickedMovie = i # sets the picked movie variable to the index of that movie in the movie array
                            movieHover[i] = False # sets the movie hover boolean back to false
                            timeSelection = True # sets the boolean that denotes the user is selecting the time to True
                            selection = True # sets the boolean that denotes that the selection window is on to True
                        elif secondThree and i!= 2: # if its not the first three movies and its not on the 3 movie (index 2 in the for loop)
                            pickedMovie = i+3 # sets the picked movie variable to the index of the movie hovered + 3 (since they are the second three 3 must be added so that it matches the movie's index in the array of movies)
                            selection = True # sets the boolean that the user is on the selection window to true
                            timeSelection = True # sets the boolean that denotes the user is selecting the time to true
                            movieHover[i] = False # resets the moive hover boolena for this movie back to false

                for i in range(len(timeHover)): # goes through the numbers 0 till the number of times available - 1 (-1 becuase for loops count from 0 to the range -1 [ex: range(5) denotes 0 to 4, still denotes 5 loops but just starts from 0])
                    if timeHover[i] == True: # checks if the current index has the time hovered alogn with a click 
                        pickedTime = timeInfo[i] # if so the picked time variable is set to the string of the time picked
                        timeSelection = False # this sets the boolean denoting the user is picking the time to False
                        seatSelection = True # this sets the boolean denoting the user is now picking their seat to True
                        timeHover[i] = False # resets the time hovered back to false
                        totalSeatCalculated = False # sets the variable denoting the seat info has been retrieved to False
                
                if seatSelection: # if the user is currently picking their seats
                    for y in range(len(hoveredSeat)): # for loop that goes through the rows of the hovered seat 2d list
                        for x in range(10): # for loop that goes through the coloumns in each row of the hovered seats 2d list 
                            if hoveredSeat[y][x] == 1: # checks the seat at the position the for loop is currently checking is hovered during the click
                                if [y,x] in pickedSeats: # if it checks if the seat is already in the picked seats list
                                    pickedSeats.remove([y,x]) # if so that means the user is removing the seat (thus the seat is removed from the list)
                                else: # if the seat is not in the picked seats list already
                                    if seatsSelected < 11: # checks to make sure the the number of seats selected is still less than 11 (maximum 10 then)
                                        pickedSeats.append([y,x]) # if it is less than 10, the seat is added to the picked list

                    seatsSelected = len(pickedSeats) # resets the variable denoting the number of seats selected to the new length of picked seats (in case it changed)

                if seatContinue and seatSelection and len(pickedSeats) > 0:  # checks if the continue button is hovered on the seat selection page and that the user is currently on the seat selection page and that hte user picked more than 0 seats
                    seatSelection = False # sets the boolean denoting the user is selecting seats to false
                    signInPage = True # sets the boolean that the user is on the sign up / sign in page to True
                    seatContinue = False # sets the boolean denoting that the continue button in seat selection step is hovered to False
                    username = usernameDefault # resets the username 
                    password = passwordDefault # resets the password
                    creditCard = creditcardDefault # resets the credit card info
                    email = emailDefault # resets the email info

                if signInPage: # if the user is currently on the sign up/ sign in page
                    if signUpHover: # if the user is hovering over the sign up buttom during the button click
                        if signUpPage != True: # checks if the sign up page is not already the one being displayed
                            signUpPage = True # if it isnt, then it the boolean denoting it is on is set to true
                            username = usernameDefault # resets the username variable
                            password = passwordDefault # resets the password variable
                            creditCard = creditcardDefault # resets the credit card variable 
                            email = emailDefault # resets the email variable
                        elif checkInfo('signup'): # if the page is already open, and the user is hovering the sign up button and clicks, then it checks if the info is correctly formatted (for signing up)
                            if upd.update().addUser(username, password, creditCard, email): # if the info is formatted right, it then tries to add the user info using the update() class in the updateScript in this directory and the add user function
                                # if it succeeds
                                signInPage = False # sets the boolean denoting that the user is on hte sign in page to False
                                for seats in range(len(pickedSeats)): # goes through all the seats in the picked seats (using the index number stored in seats)
                                    row = pickedSeats[seats][1] # sets the variable row to the row of the currently picked seat
                                    coloumn = pickedSeats[seats][0] # sets the variable coloumn to the coloumn of the currently picked seat
                                    upd.update().bookSeat(pickedTime, row, coloumn, pickedMovie) # it then books the seat for the user using the bookSeat() function in the update class in the update script in the directory
                                    upd.update().addPoints(username, password) # it then also uses another function in the update script (addPoints()) to award the user points for every chair selected
                                ticketOut = True # sets the boolean denoting the user is currently on the ticket viewing page to true
                            else: # if the addUser method returns false (fails to add the user to the list) that means the user already existed
                                print("already exists") # sends it out to the console (not seen by the user using the application)
                    
                    elif signInContinue: # if the button hovered and clicked is instead the sign in button
                        if signUpPage: # checks if the user is on the sign up page not sign in
                            # takes the user to the sign in page
                            signUpPage = False # sets the boolean denoting the user is on the sign up page to False
                            emailTyping = False # sets the boolean denoting the user is typing their email to False
                            cardTyping = False  # sets the boolean denoting the user is typing their credit card info to False
                            username = usernameDefault # resets the username string
                            password = passwordDefault # resetns the password string
                            creditCard = creditcardDefault # resets the credit card info string
                            email = emailDefault # resets teh email string
                        elif checkInfo('signin'): # checks if the info is formatted corrently (for signing in)
                            if upd.update().checkUser(username, password): # uses the update class and checkUser method to check if the username and password exist and match each other
                                # if they do match
                                signInPage = False # this sets the boolean representing the user is on the sign up / sign in part of the process to False
                                signUpPage = False # sets the boolean denoting the user is on the sign up page to False
                                for seats in range(len(pickedSeats)): # goes through all the seats in the picked seats
                                    row = pickedSeats[seats][1] # sets the var row to the row of the current picked seat
                                    coloumn = pickedSeats[seats][0] # sets the var coloumn to the coloumn of the current picked seat
                                    upd.update().bookSeat(pickedTime, row, coloumn, pickedMovie) # it then books the seat for the user using the bookSeat() function in the update class in the update script in the directory 
                                    upd.update().addPoints(username, password) # it then also uses another function in the update script (addPoints()) to award the user points for every chair selected
                                ticketOut = True # sets the boolean denoting the user is currently on the ticket viewing page to true
                            else: # if the username and password do not exist in the data base or do not match
                                print("Wrong info") # does not change the page (waits for user to enter correct info) and prints in the console wrong info (not for user to see)

                    
                    if mousePos[0] > int(width/2 - 200) and mousePos[0] < int(width/2 +200): # if the user is on the sign up or sign in page, and they are within the boundries of all the info typing fields
                        if mousePos[1] > int(height/2 - 110) and mousePos[1] < int(height/2 - 65): # if the mouse is over the first field (username)
                            userTyping = True # boolean for username typing is set to True
                            username = '' # username string is set to and empty string
                        else:
                            userTyping = False # else the userTyping is set to false
                        
                        if mousePos[1] > int(height/2 - 30) and mousePos[1] < int(height/2 + 15): # checks if it is over the second field (password)
                            passTyping = True # if so password typing boolean is set to True
                            password = '' # password string is set to an empty string
                        else:
                            passTyping = False # else the password typing boolean is set to False
                        
                        if signUpPage: # if the user is on the sign up page (has more fields)
                            if mousePos[1] > int(height/2 + 50) and mousePos[1] < int(height/2 + 95): # if the user is hovering the 3rd field (credit card info)
                                cardTyping = True # credit card info boolean typing is set to True
                                creditCard = '' # credit card string is set to an empty string
                            else:
                                cardTyping = False # else the credit card info typing boolean is set to False
                            
                            if mousePos[1] > int(height/2 + 130) and mousePos[1] < int(height/2 +175): # if the mouse is hovering hte last field (4th; email)
                                emailTyping = True # boolean for typing email is set to True
                                email = '' # email string is set to an empty string
                            else:
                                emailTyping = False # else the boolean for typing email is set to False
                    else: # if the user is not over the the feilds horizontally using their mouse, they are all set to false 
                        userTyping = False
                        passTyping = False
                        cardTyping = False
                        emailTyping = False

                if not maximized: # if the window was not maximized
                    if draggingWin == False: # and the window is not currently being moved / dragged
                        mousePos = pygame.mouse.get_pos() # retrieves mousePos (most recent one [executing the commands before this mean that mouse might be in a different position by now])
                        if mousePos[0] > 0 and mousePos[0] < width-120 and mousePos[1] > 0 and mousePos[1] < 25: # if the mouse is over the border
                            draggingWin = True # sets the boolean denoting that the window is being dragged to True 
                            oldPos = pygame.mouse.get_pos() # sets the starting point for dragging to the mouse's current position
        
        elif event.type == MOUSEBUTTONUP: # checks if the event was a mouse button being released
            if event.button == 1: # the left mouse button is released
                if not maximized: # if the window is not maximized
                    if draggingWin: # and the window is being dragged
                        draggingWin = False # then set boolean denoting the window is being dragged to false
                        mousePos = pygame.mouse.get_pos() # get the most recent mouse position
                        winPos = (winPos[0] - oldPos[0] + mousePos[0], winPos[1] - oldPos[1] + mousePos[1]) # update the new position of the window based on old position of the mouse and its current position
                        window.position = winPos # set the new window position to the calculated one

        if event.type == MOUSEMOTION: # checks if the event was mouse motion
            if not maximized: # if the window is not maximized
                if draggingWin: # and the window is being dragged
                    mousePos = pygame.mouse.get_pos() # then get the mouse recent mouse position
                    winPos = (winPos[0] - oldPos[0] + mousePos[0], winPos[1] - oldPos[1] + mousePos[1]) # calculate the new window position
                    window.position = winPos # set the new window position to the calculated one
                    
    
    # background of everything
    root.fill((57, 237, 222)) # fills in the background of the whole window th the colour (57, 237, 222) [light green in the back]

    #border
    #border - background
    draw.rect(root, (40, 184, 153), (0,0, width, 25)) # draws a rectangle using the draw.rect method in the pygame library that has a colour of (40,184, 153) and starts at 0,0 and its width is the width of the screen, and its height is 25 pixels

    #border - elements
    #elements - x

    # checks the hvoer states for each button to to set their colours
    if hoverStates[0]: # if x is being hovered
        colourX = (255,255,255) # sets the icon colour to white (255)
        colourXback = (242, 27, 27) # and the background to (242, 27, 27)
    else: # if the x is not being hovered
        colourX = (125, 245, 219) # sets the icon colour to (125, 245, 219)
        colourXback = (40, 184, 153) # and sets the background colour to the colour of the border (40, 184, 153)

    #elements - square
    if hoverStates[1]: # if the square is being hovered
        colourSquareBack = (65, 209, 178) # sets the background colour of the square
        colourSquare = (255,255,255) # icon colour
    else:
        colourSquare = (125, 245, 219) # icon colour if not hovered
        colourSquareBack = (40, 184, 153)  # background colour if not hovered (border colour)
    
    #elements - minus 
    if hoverStates[2]: # if minus is being hovered
        colourMinusBack = (65, 209, 178) # background colour if minus is hovered
        colourMinus = (255,255,255) # icon colour if hovered
    else:
        colourMinus = (125, 245, 219) # icon colour if not hovered
        colourMinusBack = (40, 184, 153) # background colour if not hovered (border colour)
    
    #colours array
    borderColours = [[colourX, colourXback], [colourSquare, colourSquareBack], [colourMinus, colourMinusBack]] # adds the colours to a 2D array that can be used later on with each element being an array, ordered such that first is x, second is squrae third is minus, with each holding the background and icon colours

    for i in range(1,4): # loops through numbers 1 to 3 to go through the icons and draw their background rect along with the icons them selves
        draw.rect(root, borderColours[i-1][1], (width-(i*40),0, 40, 25)) # draws the background rectangle for the icon
        currBorderImage = colourImage(borderImages[i-1], borderColours[i-1][0][0],borderColours[i-1][0][1], borderColours[i-1][0][2], borderColours[i-1][1]) # recolours the image being drawn using the colour image function at the top, returns new image to the variable
        root.blit(currBorderImage, (width-(i*40),0)) # blit (method used to combine surfaces or images in pygame [it is also used in computers where "bitmaps" are combined, which are basically images made of dots or pixels each pixel having its own value and in pygame's case they are refered to by the pygame library documentation as surfaces])
        # essentially the image is added onto the window (reffered to as root) at the specified position

    #Main Display
    # This commented code adds the wave shape in the background (Too laggy as it isnt an image / shape so its commented out)
    # for x in range(width):
    #     for y in range(int(height/10)+50):
    #         if y > (50*math.sin((1/200)*x)+50):
    #             draw.rect(root, (255,255,255), (x+1, y+400, 1, 1))
    # isntead I use a simple rectangle as bellow
    # Background
    # Background - Rectangle Shape
    draw.rect(root, (255,255,255), (0, 5 * height/ 8, width, height))

    # Main Page
    if mainPage == True: # if the user is on the main page
        # Main - Background - Images
        # displays the background images
        tempBackImage = pygame.transform.scale(backImage, (round(1920 * (width/1920)), round(1080 * (height/1080)))) # scales the images to match window size and assigns them to a temporary var
        root.blit(tempBackImage, (0,0)) # images added to the window

        # Title
        root.blit(titleImage, (width/2 - 250,0)) # the title of the movie theatre is added onto the window

        # Button
        if enterButtonHover == True: # checks if the enter button is hovered to switch between the possible colours for it using i to indicate which colour
            i = 1
        else:
            i = 0
        buttonBackColors = enterButtonColors[i]
        draw.rect(root, buttonBackColors[0], (width/2-245, height/2+5, 500, 100), border_radius= 4) # draws the shadow rectangle using the colours currently picked
        draw.rect(root, buttonBackColors[1], (width/2-250, height/2, 500, 100), border_radius= 4) # draws the rectangle using the colours currently picked

        # Button - Text
        enterButtonText = font.render('ENTER', True, (255,255,255), buttonBackColors[1]) # creates a surface with the text "ENTER" using the stored font (font family + size) that was iniatilized as font at the start
        enterButtonRect = enterButtonText.get_rect() # this gets the rectangle that surrounds the text (will be used to place text using the wanted center point)
        enterButtonRect.center = (int(width/2), int(height/2)+50) # this sets the wanted center point for the text (it is set to the rectangle that is gotten from the text)
        root.blit(enterButtonText, enterButtonRect) # places the text at the position of the rectangle that we set using the center point

    # Movie Page
    elif moviePage == True: # if the movie page is on instead
        # Logo
        tempTitle = pygame.transform.scale(titleImage, (200, 200)) # scales down the title image / logo to 200 x 200 pixels
        root.blit(tempTitle, (0,-30)) # places it in the top left corner
        
        # Title
        # similar to the enter text this displays the title of the page for movies which is Movies
        titleText = font.render('MOVIES', True, (20,64,255), (57, 237, 222))
        titleTextRect = titleText.get_rect()
        titleTextRect.center = (int(width/2), 200)
        root.blit(titleText, titleTextRect)
        
        # Sliding animation
        if movieSlidingAnim1: # if the first sliding animation is on
            if slidingFactor1 > -(width): # as long as the sliding factor is still greater than the negative of the width
                slidingFactor1 -= 50 # it is reduced by 50 (moves the movies by 50 px to the left every loop)
            else:
                slidingFactor1 = 0 # when the animation is over the sliding factor is set to 0 (reset)
                firstThree = False # the first three movies are set to False
                secondThree = True # second three movies are displayed
                movieSlidingAnim1 = False # animation is set to false
        
        if movieSlidingAnim2: # if its the second animation that is on
            if slidingFactor1 < (width): # as long as the sliding factor is less than the width size
                slidingFactor1 += 50 # the sliding factor is increased by 50 (movies movie to the right by 50 px)
            else:
                slidingFactor1 = 0 # resets the sliding factor to 0
                secondThree = False # sets the second three movies to false
                firstThree = True # sets the first three movies to True
                movieSlidingAnim2 = False # sets the animation to False

        # Movies
        if firstThree == True: # if its the first three movies
            for i in range(3):
                # it displays the movie (each having the slidingfactor variable added such that they move once animation starts)
                currMovImg = pygame.transform.scale(movieImages[i], (270,405))
                root.blit(currMovImg, (int((i+1)*width/4 - 135 + slidingFactor1),int(1*height/4)+100))

            if movieSlidingAnim1 != True: # if the animation is not happening for the first slide
                for i in range(len(movieHover)): # goes through the movies
                    # if they are hovered
                    if movieHover[i]:
                        # it creates a surface with a transperrancy of 240 that is not completely white (245 not 255)
                        hoverRect = pygame.Surface((270,405))
                        hoverRect.set_alpha(240)
                        hoverRect.fill((245,245,245))
                        root.blit(hoverRect, (int((i+1) * width/4 - 135 + slidingFactor1),int(1*height/4)+100))

                        # stores information about the movie hovered into an array
                        currInfo = movieInfo[i]
                        lines = [f"Screen #: {i+1}", f"Name: {currInfo['name']}", f"Genre: {currInfo['genre']}", f"Seats #: {currInfo['seats']}", f"Time: {currInfo['time']}hrs"]
                            
                        # uses a for loop to go through the array and display each line on top of the rectangle created
                        for j in range(len(lines)):
                            movieText = font2.render(lines[j], True, (20,64,255))
                            movieTextRect = titleText.get_rect()
                            movieTextRect.center = (int((i+1) * width/4), int(1*height/4)+ 135 + 40*(j+1))
                            root.blit(movieText, movieTextRect)
        
        # if its second three movies
        elif secondThree == True:
            for i in range(2): # display the 2 movies on this page
                currMovImg = pygame.transform.scale(movieImages[i+3], (270,405))
                root.blit(currMovImg, (int((i+1) * width/4 - 135 + slidingFactor1),int(1*height/4)+100))

            if movieSlidingAnim2 != True: # if the movie animation is not happening
                for i in range(len(movieHover)): # it goes through the hovered movie array and checks if they are hovered
                    if i != 2:
                        if movieHover[i]:
                            # creates a rectangle surface that is semi transparent on top of hovered movie to display info
                            hoverRect = pygame.Surface((270,405))
                            hoverRect.set_alpha(240)
                            hoverRect.fill((245,245,245))
                            root.blit(hoverRect, (int((i+1) * width/4 - 135 + slidingFactor1),int(1*height/4)+100))
                            
                            #stores info for the movie in a list
                            currInfo = movieInfo[i+3]
                            lines = [f"Screen #: {i+4}", f"Name: {currInfo['name']}", f"Genre: {currInfo['genre']}", f"Seats #: {currInfo['seats']}", f"Time: {currInfo['time']}hrs"]
                                
                            # goes through the list and displays each line
                            for j in range(len(lines)):
                                movieText = font2.render(lines[j], True, (20,64,255))
                                movieTextRect = titleText.get_rect()
                                movieTextRect.center = (int((i+1) * width/4), int(1*height/4)+ 135 + 40*(j+1))
                                root.blit(movieText, movieTextRect)

                    
        # Slider
        # checks if the slider is beign hovered and sets the colours based on that
        if sliderHover:
            sliderColor = sliderColours[0]
        else:
            sliderColor = sliderColours[1]

        # draws the slider in the right position based on if its the first or second movie page
        if firstThree == True:
            draw.polygon(root, sliderColor, [(width - 100, int(1*height/4)+303), (width-130, int(1*height/4)+333), (width-130, int(1*height/4)+273)])
        else:
            draw.polygon(root, sliderColor, [(100, int(1*height/4)+303), (130, int(1*height/4)+333), (130, int(1*height/4)+273)])
    
        # selection background
        # if the user selected a movie, and now selecting specifics
        if selection:
            # draws a semi transparent layer on top of the whole page
            select = pygame.Surface((width,height))
            select.set_alpha(200)
            select.fill((235,235,235))
            root.blit(select, (0, 25))
            # adds a window that is used so the user is able to select the info
            draw.rect(root, (255,255,255), (int(width/2 - 250), int(height/2 - 250), 500, 500), border_radius= 10)
        
            # time selection
            if timeSelection: # if the user is selecting the time 
                # displays the title
                timeTitleText = font.render('Times', True, (20,64,255))
                timeTitleTextRect = timeTitleText.get_rect()
                timeTitleTextRect.center = (int(width/2), int(height/2 - 180))
                root.blit(timeTitleText, timeTitleTextRect)

                # goes through all the times
                for i in range(len(timeInfo)):
                    # if the time is hovered, it changes the background border colour
                    if timeHover[i] == True:
                        timeBorderColor = (210, 210, 210)
                    else:
                        timeBorderColor = (235, 235, 235)

                    # displays the times one after the other (under each other)
                    draw.rect(root, timeBorderColor, (int(width/2 - 60), int(height/2 - 115 + i*70), 120, 50), border_radius= 25)
                    timeText = font2.render(timeInfo[i], True, (0,0,0))
                    timeRect = timeText.get_rect()
                    timeRect.center = (int(width/2), int(height/2 - 90 + (i*70)))
                    root.blit(timeText, timeRect)

            # Seat selection
            if seatSelection: # if the user is currently selecting their seats
                if totalSeatCalculated != True: # if the seat info is not already retrieved
                    # it uses the update script in the directory to retieve the info
                    seatInfo = upd.update().seatInfo(pickedTime, pickedMovie)
                    allSeatInfo = seatInfo['all']['seats']
                    availableAllInfo = seatInfo['all']['available']
                    disableSeatInfo = seatInfo['disablity']['seats']
                    availableDisableInfo = seatInfo['disablity']['available']
                    totalSeatCalculated = True # sets the boolean denoting that the seat info has already been retrieved

                priceText = font2.render(f"Price: {seatsSelected * 10} CAD", True, (0,0,0)) # adds text bottom left that displays the total price so far
                root.blit(priceText, (int(width/2 - 240), int(height/2 + 220)))

                # checks if the user is hovering the continue button to select its colours
                if seatContinue: 
                    colourCont = (3, 86, 252)
                    colourText = (255,255,255)
                else:
                    colourCont = (255,255,255)
                    colourText = (3, 86, 252)
                # draws the border for the continue border
                draw.rect(root, colourCont, (int(width/2 + 90), int(height/2 + 190), 150, 50), border_radius= 30)

                # dispalys the text for continue button
                priceText = font2.render(f"Continue >", True, colourText)
                root.blit(priceText, (int(width/2 + 120), int(height/2 + 200)))

                # variables that denote the starting points for the seats in x and y
                seatStartingX = int(width/2 - 220)
                seatStartingY = int(height/2 - 230)

                # nested for loop to tranverse the retireved info on each chair to check if hte chair is empty or not
                for coloumns in range(8):
                    # non-disablity seats
                    for seat in range(allSeatInfo[coloumns]):
                        if availableAllInfo[seat][coloumns] == "True":
                            # if the seat is clear in the database
                            if (mousePos[0] > seatStartingX + (coloumns * 60) and mousePos[0] < seatStartingX + (coloumns * 60) + 25 and mousePos[1] > seatStartingY + (seat * 40) and mousePos[1] < seatStartingY + (seat * 40) + 25):
                                 # if its hovered, the the relative position to that seat in the 2D hoveredSeat array is set to 1, and the colour is changed
                                 seatColour = (50,50,50)
                                 hoveredSeat[coloumns][seat] = 1
                            else:
                                # if the seat is not hovered then it has the normal colour, and the relative position in the 2D hovered seat array is set to 0 (denotes not)
                                seatColour = (20,64,255)
                                hoveredSeat[coloumns][seat] = 0
                            if ([coloumns,seat] in pickedSeats):
                                # if the seat is already in the picked seats, it remains selected and is denoted using a differnt colour
                                seatColour = (70,70,70)
                        else:
                            seatColour = (255,0,0) # if the seat is not available, it scolour is set to false
                        
                        # finally it draws the seat using the colour and location
                        draw.rect(root, seatColour, (seatStartingX + (coloumns * 60), seatStartingY + (seat * 40), 25,25), border_radius= 2)


                    # disability seats
                    # after going through the normal seatings, it goes through the disability seats
                    for seat in range(allSeatInfo[coloumns], allSeatInfo[coloumns]+disableSeatInfo[coloumns]):
                        if availableDisableInfo[seat-allSeatInfo[coloumns]][coloumns] == "True": # if the seat is not taken
                            if (mousePos[0] > seatStartingX + (coloumns * 60) and mousePos[0] < seatStartingX + (coloumns * 60) + 25 and mousePos[1] > seatStartingY + (seat * 40) and mousePos[1] < seatStartingY + (seat * 40) + 25):
                                 # colour is changed if the seat is hovered, and that seat is represented as hovered in the hoveredSeat 2D array
                                 seatColour = (50,50,50)
                                 hoveredSeat[coloumns][seat] = 1
                            else:
                                # if the seat is not hovered, then its set to the colour that denotes seats for people with a disability
                                seatColour = (255,64,255)
                                # seat is represented as not hovered in the hovered Seat 2D array
                                hoveredSeat[coloumns][seat] = 0
                            
                            # if the seat is already in the picked seats
                            if ([coloumns,seat] in pickedSeats):
                                # it's denoted using a specific colour
                                seatColour = (70,70,70)
                        else:
                            # if the seat is taken, then its colour is red
                            seatColour = (255,0,0)

                        # the seat is drawn uisng the colour and location
                        draw.rect(root, seatColour, (seatStartingX + (coloumns * 60), seatStartingY + (seat * 40), 25,25), border_radius= 2)


            # Sign In
            if signInPage:
                # colours for sign in button are configured based on if the button is hovered or not
                if signInContinue:
                    colourSignIn = (3, 86, 252)
                    colourSignInText = (255,255,255)
                else:
                    colourSignIn = (255,255,255)
                    colourSignInText = (3, 86, 252)

                # the button is drawn
                draw.rect(root, colourSignIn, (int(width/2 + 90), int(height/2 + 190), 150, 50), border_radius= 30)

                # the text for the button is placed
                priceText = font2.render(f"Sign In >", True, colourSignInText)
                root.blit(priceText, (int(width/2 + 130), int(height/2 + 200)))

                # the colours for the sign up button ar econfigured based on if the button is hovered or not
                if signUpHover:
                    colourSignUp = (3, 86, 252)
                    colourSignUpText = (255,255,255)
                else:
                    colourSignUp = (255,255,255)
                    colourSignUpText = (3, 86, 252)

                # draws the sign up button
                draw.rect(root, colourSignUp, (int(width/2 - 240), int(height/2 + 190), 150, 50), border_radius= 30)
                # displays sign up text
                priceText = font2.render(f"< Sign Up", True, colourSignUpText)
                root.blit(priceText, (int(width/2 - 210), int(height/2 + 200)))

                # if the user is on the sign up page
                if signUpPage:
                    # the text title becomes sign up instead
                    pageTitleText = font.render('Sign Up', True, (20,64,255))

                    # Credit Card box is displayed
                    draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 + 50), 400, 45))
                    creditText = font2.render(creditCard, True, (20,64,255))
                    root.blit(creditText, (int(width/2 - 190), int(height/2 + 60)))

                    # Email box is displayed
                    draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 + 130), 400, 45))
                    emailText = font2.render(email, True, (20,64,255))
                    root.blit(emailText, (int(width/2 - 190), int(height/2 + 140)))
                else:
                    # if its not the sign up page, then the teitle becomes sign in
                    pageTitleText = font.render('Sign In', True, (20,64,255))

                # Username box is displayed on sign in or sign up
                draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 - 110), 400, 45))
                userText = font2.render(username, True, (20,64,255))
                root.blit(userText, (int(width/2 - 190), int(height/2 - 100)))

                # Password box is displayed on sign in or sign up
                draw.rect(root, (230, 230, 230), (int(width/2 - 200), int(height/2 - 30), 400, 45))
                passText = font2.render(password, True, (20,64,255))
                root.blit(passText, (int(width/2 - 190), int(height/2 - 20)))
                
                # displays the title
                pageTitleRect = pageTitleText.get_rect()
                pageTitleRect.center = (int(width/2), int(height/2 - 180))
                root.blit(pageTitleText, pageTitleRect)

            # Ticket Output page
            if ticketOut:
                # sets the title text to "Reciept"
                pageTitleText = font.render('Reciept', True, (20,64,255))
                nameText = font2.render(f"Name: {username}", True, (20,64,255)) # uses username for the name text
                costText = font2.render(f"Price: {seatsSelected * 10} CAD", True, (20,64,255)) # sets the price text
                timeText = font2.render(f"Time: {pickedTime}", True, (20,64,255)) # sets the picked time text
                screenText = font2.render(f"Screen: {pickedMovie+1}; {movieInfo[pickedMovie]['name']}", True, (20,64,255)) # sets the screen and movie picked text
                seatTitleText = font2.render("Seats Picked:", True, (20,64,255)) # seats picked titel

                textArr = [nameText, costText, timeText, screenText, seatTitleText] # array of text to display

                for text in range(len(textArr)):# goes through the text array and displays it 
                    root.blit(textArr[text], (int(width/2 - 110), int(height/2 - 120 + 30 * text)))

                for seats in range(len(pickedSeats)): # at the end it adds the seats, using letters to represent the coloumns
                    row = pickedSeats[seats][1] + 1
                    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    coloumn = pickedSeats[seats][0]
                    seatText = font2.render(f"Seat {seats+1}: {alph[coloumn]}{row}", True, (0,0,0))
                    root.blit(seatText, (int(width/2 - 80), int(height/2 + 30 + 20 * seats)))

                # displays title for ticket page
                pageTitleRect = pageTitleText.get_rect()
                pageTitleRect.center = (int(width/2), int(height/2 - 180))
                root.blit(pageTitleText, pageTitleRect)

    # Refresh Display
    pygame.display.update()
    

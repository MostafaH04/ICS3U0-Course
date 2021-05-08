'''
-----------------------------------------------
| Student  :  Mostafa Hussein                 |
| Student# :  899733                          |
| Cohort   :  C                               |
| Teacher  :  Mr. Ghorvei                     |
| Subject  :  Calculator                      |
| Date     :  May 3rd 2021                    | 
-----------------------------------------------
'''
# Link to repl.it file:
# https://replit.com/@p00766641/Input-Output-Calculator-MH899733#main.py 

# Instructions:
'''
1. The program begins, prompting the user to enter their name (string)

2. The user is then asked wheather they mind or do not mind giving the program their age

3. Upon inputing the age (or skipping that process), the main page for the calculator is opened, and the user is prompted to pick one of the 13 functions displayed on the screen

------------------------------------------------------------------
Option 0: Addition (Explanation Example):

Like all other arithmatic options in the calculator, the user greeted with an animation (for fun), and upon that, based on the function the user is prompted to input one or two numbers. For addition the user will get the option to pick 2 numbers.

The output of the function is then displayed and the user is prompted with a press enter to continue. This makes sure the user saw the output, before the console is clear and the main page is displayed.

Other Options (1 - 11):

Similar to the addition function, the functions carry out the same processes for the different function, with each doing its own unique mathematical computation

Exit and History Options:

If the user picks the 12th option, they are greeted with the history of their previous calculations, which will be empty if the user did no previous calculations. Currently, this history is volatile, as it resets everytime the program resets, (no data storage system in place)

On the other hand if the user picks the 13th option, the program ends

'''


import os # Importing the OS library (to clear console)
import time # Importing time libarary 
import math # Importing math libarry 

# List storing the history of calculations

calcHis = []

# Delay between each animated letter 
animDelay = 0.4

# Function for animating text
def animate(content):
  # Uses a for loop that repeats as many times as there are letters 
  for i in range(len(content)): 
    print(content[:i]) # Prints the content in the string given to the function up until "i" number of letters, so as the for loop moves on, it prints more and more letters

    time.sleep(animDelay/len(content)) # Uses the animation delay variable divided by the length of the string, and this acts as a the delay between every letter printed in the console

    os.system("clear") # this clears the console and makes it empty
  print(f"{content}\n\n") # Prints the complete string at the end

  pass # does not return anything back to where the function was called

# Initiallizing Functions for the calculator

# Addition
def add():
  os.system("clear") # clears the console
  
  addString = "Addition" # sets a variable for addition, used for the animation of the text
  animate(addString) # calls the function for animating the text

  firstNum = float(input("First Number: ")) # Asks the user for the first number
  secondNum = float(input("Second Number: ")) # Asks the user for the second number

  print(f"\n{firstNum} + {secondNum} = ", end = "") # Prints the statement without the valeu (will be printed later)

  calcHis.append([addString, f": {firstNum} + {secondNum} = {firstNum+secondNum}"]) # Stores the calculation in the history list

  return firstNum+secondNum # Returns the sum of both numbers to be printed from where the function was called

# This function carries out the process for the subtraction
def diff():
  os.system("clear")
  
  diffString = "Subtraction"
  animate(diffString)

  firstNum = float(input("First Number: "))
  secondNum = float(input("Second Number: "))

  print(f"\n{firstNum} - {secondNum} = ", end = "")

  calcHis.append([diffString, f": {firstNum} - {secondNum} = {firstNum-secondNum}"])

  return firstNum - secondNum

# This function carries out the process for the multiplication
def multi():
  os.system("clear")
  
  multiString = "Multiplication"
  animate(multiString)

  firstNum = float(input("First Number: "))
  secondNum = float(input("Second Number: "))

  print(f"\n{firstNum} x {secondNum} = ", end = "")

  calcHis.append([multiString, f": {firstNum} x {secondNum} = {firstNum*secondNum}"])

  return firstNum * secondNum

# This function carries out the process for the division
def divide():
  os.system("clear")
  
  divideString = "Division"
  animate(divideString)

  firstNum = float(input("First Number: "))
  secondNum = float(input("Second Number: "))

  print(f"\n{firstNum} ÷ {secondNum} = ", end = " ")

  calcHis.append([divideString, f": {firstNum} ÷ {secondNum} = {firstNum/secondNum}"])

  return firstNum / secondNum

# This function carries out the process for the remainder
def modulo():
  os.system("clear")
  
  moduloString = "Remainder"
  animate(moduloString)

  firstNum = float(input("First Number: "))
  secondNum = float(input("Second Number: "))

  print(f"\nThe Remainder from the operation {firstNum} ÷ {secondNum}, is", end = " ")

  calcHis.append([moduloString, f": The Remainder from the operation {firstNum} ÷ {secondNum}, is {firstNum%secondNum}"])

  return firstNum % secondNum

# This function carries out the process for the sin function
def sine():
  os.system("clear")
  
  sineString = "Sine"
  animate(sineString)

  while True:
    radiansQ = input("Would you like to continue in radians or degrees? (r/d)\n")
    
    if radiansQ.lower() == 'r' or radiansQ.lower() == "radians":
      radians = True
      break
    
    elif radiansQ.lower() == 'd' or radiansQ.lower() == "degrees":
      radians = False
      break

  firstNum = float(input("\nTheta = "))
  
  print(f"\nsin({firstNum}) =", end = " ")

  if radians:
    
    calcHis.append([sineString, f": sin({firstNum}) = {math.sin(firstNum)}"])
    
    return math.sin(firstNum)

  else:

    calcHis.append([sineString, f": sin({firstNum}) = {math.sin(firstNum*math.pi/180)}"])

    return math.sin(firstNum*math.pi/180)    

# This function carries out the process for the cosin function
def cosine():
  os.system("clear")
  
  cosineString = "Cosine"
  animate(cosineString)

  while True:
    radiansQ = input("Would you like to continue in radians or degrees? (r/d)\n")
    
    if radiansQ.lower() == 'r' or radiansQ.lower() == "radians":
      radians = True
      break
    
    elif radiansQ.lower() == 'd' or radiansQ.lower() == "degrees":
      radians = False
      break

  firstNum = float(input("\nTheta = "))
  
  print(f"\ncos({firstNum}) =", end = " ")

  if radians:
    
    calcHis.append([cosineString, f": cos({firstNum}) = {math.cos(firstNum)}"])

    return math.cos(firstNum) 

  else:

    calcHis.append([cosineString, f": cos({firstNum}) = {math.cos(firstNum*math.pi/180)}"])

    return math.cos(firstNum*math.pi/180)    

# This function carries out the process for the tan function
def tangent():
  os.system("clear")
  
  tangentString = "Tangent"
  animate(tangentString)

  while True:
    radiansQ = input("Would you like to continue in radians or degrees? (r/d)\n")
    
    if radiansQ.lower() == 'r' or radiansQ.lower() == "radians":
      radians = True
      break
    
    elif radiansQ.lower() == 'd' or radiansQ.lower() == "degrees":
      radians = False
      break

  firstNum = float(input("\nTheta = "))
  
  print(f"\ntan({firstNum}) =", end = " ")

  if radians:

    calcHis.append([tangentString, f": tan({firstNum}) = {math.tan(firstNum)}"])

    return math.tan(firstNum)    

  else:

    calcHis.append([tangentString, f": tan({firstNum}) = {math.tan(firstNum*math.pi/180)}"])

    return math.tan(firstNum*math.pi/180)    

# This function carries out the process for the power function
def power():
  os.system("clear")
  
  powerString = "Power"
  animate(powerString)

  firstNum = float(input("Base number: "))
  secondNum = float(input("Power raised: "))

  print(f"\n{firstNum} to the power of {secondNum} =", end = " ")

  calcHis.append([powerString, f": {firstNum} to the power of {secondNum} = {firstNum**secondNum}"])

  return firstNum**secondNum

# This function carries out the process for the hyperbolic sin function
def hypsin():
  os.system("clear")
  
  hypSinString = "Hyperbolic Sine"
  animate(hypSinString)

  while True:
    radiansQ = input("Would you like to continue in radians or degrees? (r/d)\n")
    
    if radiansQ.lower() == 'r' or radiansQ.lower() == "radians":
      radians = True
      break
    
    elif radiansQ.lower() == 'd' or radiansQ.lower() == "degrees":
      radians = False
      break

  firstNum = float(input("\nTheta = "))
  
  print(f"\nsinh({firstNum}) =", end = " ")

  if radians:

    calcHis.append([hypSinString, f": sinh({firstNum}) = {math.sinh(firstNum)}"])

    return math.sinh(firstNum)   

  else:
    
    calcHis.append([hypSinString, f": sinh({firstNum}) = {math.sinh(firstNum*math.pi/180)}"])

    return math.sinh(firstNum*math.pi/180)    

# This function carries out the process for the hyperbolic cos function
def hypcos():
  os.system("clear")
  
  hypCosString = "Hyperbolic Cosine"
  animate(hypCosString)

  while True:
    radiansQ = input("Would you like to continue in radians or degrees? (r/d)\n")
    
    if radiansQ.lower() == 'r' or radiansQ.lower() == "radians":
      radians = True
      break
    
    elif radiansQ.lower() == 'd' or radiansQ.lower() == "degrees":
      radians = False
      break

  firstNum = float(input("\nTheta = "))
  
  print(f"\ncosh({firstNum}) =", end = " ")

  if radians:

    calcHis.append([hypCosString, f": cosh({firstNum}) = {math.cosh(firstNum)}"])

    return math.cosh(firstNum)

  else:

    calcHis.append([hypCosString, f": cosh({firstNum}) = {math.cosh(firstNum*math.pi/180)}"])

    return math.cosh(firstNum*math.pi/180)

# This function carries out the process for the hyperbolic tan function
def hyptan():
  os.system("clear")
  
  hypTanString = "Hyperbolic Tangent"
  animate(hypTanString)

  while True:
    radiansQ = input("Would you like to continue in radians or degrees? (r/d)\n")
    
    if radiansQ.lower() == 'r' or radiansQ.lower() == "radians":
      radians = True
      break
    
    elif radiansQ.lower() == 'd' or radiansQ.lower() == "degrees":
      radians = False
      break

  firstNum = float(input("\nTheta = "))
  
  print(f"\ntanh({firstNum}) =", end = " ")

  if radians:

    calcHis.append([hypTanString, f": tanh({firstNum}) = {math.tanh(firstNum)}"])

    return math.tanh(firstNum)
  else:

    calcHis.append([hypTanString, f": tanh({firstNum}) = {math.tanh(firstNum*math.pi/180)}"])

    return math.tanh(firstNum*math.pi/180)

# Gets the user's name
name = input("Hello, what is your name?\n") 

while True:
  #Prints users name before the sentence (in a different way)
  print(f'\nAlright {name}', end = ", ")

  # Asks the user if they want to input their age
  ageQ = input(f"do you mind telling me your age?\ny/n: ") 

  # Initially sets the age to None, but if the user 
  age = None
  if ageQ.lower() == 'no' or ageQ.lower() == 'n':
    # Prints users name before the sentence (in a different way)
    print(f'\nAlright {name}', end = ", ")

    # Gets the user's age
    age=input(f"\nwhat is your age?\n")
    break

    # if the user said that they do mind, continue
  elif ageQ.lower() == 'yes' or ageQ.lower() == "y":
    break

# String including the ASCII title art (Calculator)
title = r"""
 ____            ___                  ___            __                     
/\  _`\         /\_ \                /\_ \          /\ \__                  
\ \ \/\_\    __ \//\ \     ___  __  _\//\ \      __ \ \ ,_\   ___   _ __     
 \ \ \/_/_ /'__`\ \ \ \   /'___/\ \/\ \\ \ \   /'__`\\ \ \/  / __`\/\`'__\   
  \ \ \L\ /\ \L\.\_\_\ \_/\ \__\ \ \_\ \\_\ \_/\ \L\.\\ \ \_/\ \L\ \ \ \/   
   \ \____\ \__/.\_/\____\ \____\ \____//\____\ \__/.\_\ \__\ \____/\ \_\ 
    \/___/ \/__/\/_\/____/\/____/\/___/ \/____/\/__/\/_/\/__/\/___/  \/_/          
"""

# List of possible functions
functions = ["Addition", "Subtraction", "Mulitplication", "Division", "Remainder", "Sine", "Cosine", "Tangent", "Power", "Hyperbolic Sine","Hyperbolic Cosine", "Hyperbolic Tangent", "History", "Exit"]

# User picks the function they want to use, this loop only breaks if the user wants to end the program
while True:
  # Clears the console
  os.system('clear')

  # Displays the title "Calculator at the top of the screen.
  # If not seen, make sure the console is big enough for it to be displayed properly
  print(title,end = "\n\n\n")

  # Displays the functions
  for i in range(len(functions)):

    # If the function being printed is a factor of 4, that means it is the 4th in the line so start a new line
    if i%4 == 0:print("\n")
    
    # Prints the number of the function then the function it self with spacing after it
    print(i, functions[i],end = "   ")
  print("\n\n")

  # Infinite loop that makes sure the user is inputing an applicable number
  while True:
    # Displays the question prompting the user to choose a function and stores the answer
    func = int(input(f"Pick a function between 0 and {len(functions)-1}:\n"))

    # Makes sure the user is inputing an applicable number
    if func >= 0 and func <= len(functions)-1:
      break
  
  # If the user picked 0, this calls on the addition function
  if func == 0:
    print(add())
  
  # If the user picked 1, this calls on the subtraction function
  elif func == 1:
    print(diff())

  # If the user picked 2, this calls on the Mulitplication function
  elif func == 2:
    print(multi())
  
  # If the user picked 3, this calls on the Dividsion function
  elif func == 3:
    print(divide())
  
  # If the user picked 4, this calls on the Remainder / Modulo function
  elif func == 4:
    print(modulo())
  
  # If the user picked 5, this calls on the Sine function
  elif func == 5:
    print(sine())
  
  # If the user picked 6, this calls on the Cosine function
  elif func == 6:
    print(cosine())
  
  # If the user picked 7, this calls on the Tangent function
  elif func == 7:
    print(tangent())
  
  # If the user picked 8, this calls on the power function
  elif func == 8:
    print(power())

  # If the user picked 9, this calls on the Hypoerbolic Sin function
  elif func == 9:
    print(hypsin())
  
  # If the user picked 10, this calls on the Hyperbolic cosine function
  elif func == 10:
    print(hypcos())

  # If the user picked 11, this calls on the Hyperbolic Tangent function
  elif func == 11:
    print(hyptan())
  
  elif func == 12:
    os.system("clear")
    for i in range(len(calcHis)):
      print(i+1, calcHis[i][0], calcHis[i][1])


  # If the user picked 12, this ends the program.
  elif func == 13:
    os.system("clear")
    print(f"Good night! {name} :)")
    break

  # Promts the user to type Enter in order to continue (makes sure the calculation is there until the user is done looking at it)
  continueQ = input("\n\n\nPress Enter To Continue")
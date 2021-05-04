'''
-----------------------------------------------
| Student  :  Mostafa Hussein                 |
| Student# :  899733                          |
| Cohort   :  C                               |
| Teacher  :  Mr. Ghorvei                     |
| Subject  :  Input Output - Calculator       |
| Date     :  May 3rd 2021                    | 
-----------------------------------------------
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
  #Goes through
  for i in range(len(content)):
    print(content[0:i])
    time.sleep(animDelay/len(content))
    os.system("clear")
  print(f"{content}\n\n")

  pass

#Functions for the calculator

# Addition
def add():
  os.system("clear")
  
  addString = "Addition"
  animate(addString)

  a = float(input("First Number: "))
  b = float(input("Second Number: "))

  print(f"\n{a} + {b} = ", end = "")

  calcHis.append([addString, f": {a} + {b} = {a+b}"])

  return a+b

# Subtraction
def diff():
  os.system("clear")
  
  diffString = "Subtraction"
  animate(diffString)

  a = float(input("First Number: "))
  b = float(input("Second Number: "))

  print(f"\n{a} - {b} = ", end = "")

  calcHis.append([diffString, f": {a} - {b} = {a-b}"])

  return a - b

# Multiplication
def multi():
  os.system("clear")
  
  multiString = "Multiplication"
  animate(multiString)

  a = float(input("First Number: "))
  b = float(input("Second Number: "))

  print(f"\n{a} x {b} = ", end = "")

  calcHis.append([multiString, f": {a} x {b} = {a*b}"])

  return a * b

# Division
def divide():
  os.system("clear")
  
  divideString = "Division"
  animate(divideString)

  a = float(input("First Number: "))
  b = float(input("Second Number: "))

  print(f"\n{a} ÷ {b} = ", end = " ")

  calcHis.append([divideString, f": {a} ÷ {b} = {a/b}"])

  return a / b

# Remainder
def modulo():
  os.system("clear")
  
  moduloString = "Remainder"
  animate(moduloString)

  a = float(input("First Number: "))
  b = float(input("Second Number: "))

  print(f"\nThe Remainder from the operation {a} ÷ {b}, is", end = " ")

  calcHis.append([moduloString, f": The Remainder from the operation {a} ÷ {b}, is {a%b}"])

  return a % b

# Sine
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

  a = float(input("\nTheta = "))
  
  print(f"\nsin({a}) =", end = " ")

  if radians:
    
    calcHis.append([sineString, f": sin({a}) = {math.sin(a)}"])
    
    return math.sin(a)

  else:

    calcHis.append([sineString, f": sin({a}) = {math.sin(a*math.pi/180)}"])

    return math.sin(a*math.pi/180)    

# Cosine
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

  a = float(input("\nTheta = "))
  
  print(f"\ncos({a}) =", end = " ")

  if radians:
    
    calcHis.append([cosineString, f": cos({a}) = {math.cos(a)}"])

    return math.cos(a) 

  else:

    calcHis.append([cosineString, f": cos({a}) = {math.cos(a*math.pi/180)}"])

    return math.cos(a*math.pi/180)    

# Tangent
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

  a = float(input("\nTheta = "))
  
  print(f"\ntan({a}) =", end = " ")

  if radians:

    calcHis.append([tangentString, f": tan({a}) = {math.tan(a)}"])

    return math.tan(a)    

  else:

    calcHis.append([tangentString, f": tan({a}) = {math.tan(a*math.pi/180)}"])

    return math.tan(a*math.pi/180)    

# Power
def power():
  os.system("clear")
  
  powerString = "Power"
  animate(powerString)

  a = float(input("Base number: "))
  b = float(input("Power raised: "))

  print(f"\n{a} to the power of {b} =", end = " ")

  calcHis.append([powerString, f": {a} to the power of {b} = {a**b}"])

  return a**b

#Hypoerbolic sine
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

  a = float(input("\nTheta = "))
  
  print(f"\nsinh({a}) =", end = " ")

  if radians:

    calcHis.append([hypSinString, f": sinh({a}) = {math.sinh(a)}"])

    return math.sinh(a)   

  else:
    
    calcHis.append([hypSinString, f": sinh({a}) = {math.sinh(a*math.pi/180)}"])

    return math.sinh(a*math.pi/180)    

#Hypoerbolic cosine
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

  a = float(input("\nTheta = "))
  
  print(f"\ncosh({a}) =", end = " ")

  if radians:

    calcHis.append([hypCosString, f": cosh({a}) = {math.cosh(a)}"])

    return math.cosh(a)

  else:

    calcHis.append([hypCosString, f": cosh({a}) = {math.cosh(a*math.pi/180)}"])

    return math.cosh(a*math.pi/180)

#Hypoerbolic tangent
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

  a = float(input("\nTheta = "))
  
  print(f"\ntanh({a}) =", end = " ")

  if radians:

    calcHis.append([hypTanString, f": tanh({a}) = {math.tanh(a)}"])

    return math.tanh(a)
  else:

    calcHis.append([hypTanString, f": tanh({a}) = {math.tanh(a*math.pi/180)}"])

    return math.tanh(a*math.pi/180)

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

# User picks the function they want to use
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

  continueQ = input("\n\n\nPress Enter To Continue")
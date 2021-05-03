'''
-----------------------------------------------
| Student  :  Mostafa Hussein                 |
| Student# :  899733                          |
| Cohort   :  C                               |
| Teacher  :  Mr. Ghorvei                     |
| Subject  :  Calculator using Operands       |
| Date     :  May 3rd 2021 - Present          | 
-----------------------------------------------
'''
import os # Importing the OS library (to clear console)
import time # Importing time libarary 

#Functions for the calculator

# Addition
def add():
  os.system("clear")
  
  addString = "Addition"
  for i in range(len(addString)):
    print(addString[0:i])
    time.sleep(0.25)
    os.system("clear")
  print("\n\n")

  print()

  pass

# Subtraction
def diff():
  pass

# Multiplication
def multi():
  pass

# Division
def divide():
  pass

# Remainder
def modulo():
  pass

# Sine
def sine():
  pass

# Cosine
def cosine():
  pass

# Tangent
def tangent():
  pass

# Power
def power():
  pass  


# Gets the user's name
name = input("Hello, what is your name?\n") 

# Asks the user if they want to input their age
ageQ = input(f"Hello {name}, do you mind telling me your age?\ny/n: ") 

# Initially sets the age to None, but if the user 
age = None
if ageQ.lower() == 'no' or ageQ.lower() == 'n':
  age=input(f"Alright {name}, what is your age?\n")

os.system('clear')

print("""
 ____            ___                  ___            __                     
/\  _`\         /\_ \                /\_ \          /\ \__                  
\ \ \/\_\    __ \//\ \     ___  __  _\//\ \      __ \ \ ,_\   ___   _ __     
 \ \ \/_/_ /'__`\ \ \ \   /'___/\ \/\ \\ \ \   /'__`\\ \ \/  / __`\/\`'__\   
  \ \ \L\ /\ \L\.\_\_\ \_/\ \__\ \ \_\ \\_\ \_/\ \L\.\\ \ \_/\ \L\ \ \ \/   
   \ \____\ \__/.\_/\____\ \____\ \____//\____\ \__/.\_\ \__\ \____/\ \_\ 
    \/___/ \/__/\/_\/____/\/____/\/___/ \/____/\/__/\/_/\/__/\/___/  \/_/      
\n\n\n    
""")

# List of possible functions
functions = ["Addition", "Subtraction", "Mulitplication", "Division", "Remainder", "Sine", "Cosine", "Tangent", "Power","Exit"]

# Displays the functions
for i in range(len(functions)):
  if i%4 == 0:print("\n")
  print(i, functions[i],end = "   ")
print("\n\n")

# User picks the function they want to use
while True:
  while True:
    func = int(input(f"Pick a function between 0 and {len(functions)-1}:\n"))
    if func >= 0 and func <= len(functions)-1:
      break
  
  if func == 0:
    print(add())
  
  elif func == 1:
    print(diff())

  elif func == 2:
    print(multi())
  
  elif func == 3:
    print(divide())
  
  elif func == 4:
    print(modulo())
  
  elif func == 5:
    print(sine())
  
  elif func == 6:
    print(cosine())
  
  elif func == 7:
    print(tangent())
  
  elif func == 8:
    print(power())
  
  elif func == 9:
    break

  






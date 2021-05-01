'''
--------------------------------------
| Student  :  Mostafa Hussein        |
| Student# :  899733                 |
| Cohort   :  C                      |
| Teacher  :  Mr. Ghorvei            |
| Subject  :  Variable Type Pracitce |
| Date     :  April 30th 2021        |
--------------------------------------
'''
# Importing math library for trig functions
import math

lessonNum = 1.0 # Float
topic = "variables" #String
varTypes = ["str", "int", "float", "complex"] # Array
numOfTypes = len(varTypes) # Integer

# Prints info about first lesson (Variables)
print(f"Lesson {lessonNum}\nAbout {topic}\nWhere we learned about {numOfTypes} variable types which are {varTypes}") 

# Printing the complex number = e^(i(x))
def eular(x):
  # Stores the values of cos(x) and sin(x) in a and b respectively
  a,b = float(math.cos(x)), float(math.sin(x)) 
  # Creates a complex number that represents eular's identity, where e^(i*x) = cos(x) + i*sin(x)
  #e = complex(f'{a}+{b}j') 
  if b < 0:
    e=complex(f'{a}{b}j')
  else:
    e =complex(f'{a}+{b}j')
  # Prints the complex number but does not end the line (does not end with '\n' rather ends with " = ")
  print(e,end = " = e^(j*theta)") 
  
  return e # Returns the complex number

# Recieves user input until user chooses to end
while True:
  # Waits for user input in the console and stores in in the variable userInput as a string
  userInput = input()

  # Checks if the user wanted to use eular's formula, or end 

  if userInput == "eulars":
    # Gets another input from the user, converts it to a float and calls the eular's identity function using that value. The value of the function is then stored in the variable func
    func = eular(int(input()))


  elif userInput == "end":
    # This ends the infinite loop if the user specifies they want to end the script
    break


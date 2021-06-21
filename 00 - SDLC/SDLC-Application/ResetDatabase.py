############################################
#                                          #
#  Name: Mostafa Hussein                   #
#  Student Number: 899733                  #
#  Cohort: C                               #
#  Teacher: Mr. Ghorvei                    #
#  Class: ICS3U0                           #
#  Due Date: June 22nd 2021                #
#                                          #
############################################

import json # imports json library (allows python to open .json files)
import infoScript
import reference

ref = reference.refer() # gets the refence to the databse from the reference script

# function that can reset the whole database to the orginal state (to be used on at the end of each work day)
def reset():
	global ref # references the global var that references the database (to use inside the function)
	continueReset = False # boolean to that ensures the user wants to reset the database

	# loop until user enters correct input to be used
	while True:
		sureQ = input("Are you sure. Doing this will rest the state for the day, removing all of the user's information. (Y/N)\n")
		if sureQ.lower() in ["yes", 'y']:
			continueReset = True
			break
		elif sureQ.lower() in ["no", 'n']:
			continueReset = False
			break
		else: print("\nPlease use applicable inputs (Y/N)\n")

	# if the user is sure they want to reset
	if continueReset:	
		# open the jason file using 'r' (means we are only reading from it (cant edit its content))
		file = open('information.json', 'r')
		# loads the .json file formated info into the info variable as a dictionary 
		info = json.load(file)
		# closes the opened file
		file.close()

		# resets the database to contain the information inside info
		ref.set(info)
		

reset()
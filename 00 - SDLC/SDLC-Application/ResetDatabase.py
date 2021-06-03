import json
import infoScript
import reference

ref = reference.refer()

def reset():
	global ref
	continueReset = False

	while True:
		sureQ = input("Are you sure. Doing this will rest the state for the day, removing all of the user's information. (Y/N)\n")
		if sureQ.lower() in ["yes", 'y']:
			continueReset = True
			break
		elif sureQ.lower() in ["no", 'n']:
			continueReset = False
			break
		else: print("\nPlease use applicable inputs (Y/N)\n")

	if continueReset:	
		file = open('information.json', 'r')
		info = json.load(file)
		file.close()

		ref.set(info)

		infoScript.showInfo(info).screen()
		infoScript.showInfo(info).time()

reset()
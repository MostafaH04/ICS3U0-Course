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


import reference # imports references script in directory
from firebase_admin import db # imports firebase library
import hashlib # imports the hash library (encryption)

# iniates a  class
class update():
    # the function that runs when the class is called
    def __init__(self):
        self.usersRef = db.reference("/users") # sets this variable to reference the /users directory in the database
        self.timeRef = db.reference("/times") # sets this variable to reference the /times directory in the database
        self.screenRef = db.reference("screens") # sets this variable to reference the /screens directory in the database
        self.startingPoints = 10 # variable that denotes the points given on making an acc
        self.prizePoints = 5 # variable storing points per transaction
        self.timeSlots = { # dictonary that relates each time to a key for times in the database
            "09:00":"1morning",
            "10:00":"1morning",
            "13:00":"2afternoon",
            "15:00":"2afternoon",
            "20:00":"3evening"
        }
    
    # function taht goes through the database and returns all the usernames for all the users
    def getUsers(self):
        users = self.usersRef.get()
        usernames = []
        for keys in users.keys(): # in dictionaries they have "keys" which can be retrieved using .keys() method in python, this for loops retrieves all of these keys can uses each one since each one stands for each user
            usernames.append(users[keys]["username"])
        return usernames
    
    # function that adds a user to the database using a password, username, credit card and email
    def addUser(self, newUsername, newPassword, creditCard, userEmail):
        try: # attempts to carry out the function of adding users
            users = self.getUsers()
            if newUsername in users: # if the user already exists
                return False # return false, since two users with same usernames cannot happen

            creditCardBytes = str(creditCard).encode() # insures credit card is a string, then encodes it into bytes that are used by python (required for Hash to work)
            creditHashBin = hashlib.sha256(creditCardBytes) # uses the sha256 hash function on the bytes string representing the credit card number (basically encrypting it [non-reversable]
            creditHash = creditHashBin.hexdigest() # converts the encoded data in the byte format into a hexadecimal format (better than binary in this case; results in smaller strings of infomation)
            points = self.startingPoints
            newUserData = {
                "username": newUsername,
                "password": newPassword,
                "points": points,
                "credit-card-hash": creditHash,
                "email": userEmail
            }
            self.usersRef.push(newUserData)
            return True
        
        except: # if error eccurs it returns false instead (denoting that it was not able to add the user)
            return False

    # using the given username and password, it checks if the user exists in the database with the same information
    def checkUser(self, username, password):
        users = self.usersRef.get()
        for key in users.keys():
            if username == users[key]["username"]:
                if password == users[key]["password"]:
                    print("Successful")
                    return True

        print("Not Successful, Try Again")
        return False

    # displays the seats in the console
    def disp(self, seats):
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                out = seats[y][x]
                if out == 3:
                    out = " "
                print(out, end = " ")
            print()

    # retrieves seat info from the database
    def seatInfo(self,time,screen):
        times = self.timeRef.get()

        possibleTimes = self.timeSlots.keys()
        if time not in possibleTimes:
            return "This time slot does not exist"
        
        seatData = times[self.timeSlots[time]][time][int(screen)]
        return seatData

    # uses the seatInfo function to turn the seats info into a 2d array with 1 as normal seat, 2 as disability, 3 if it does not exist and 0 if its taken
    def checkSeats(self, time, screen):
        seatData = self.seatInfo(time, screen)

        seats = []
        totalSeats = []
        seatStatus = []

        for key in seatData.keys():
            seats.append(seatData[key]["seats"])
            available = seatData[key]["available"]

            for seatRow in available:
                currRow = []

                for seat in seatRow:
                    if seat == "True":
                        if key == "disablity":
                            currRow.append(2)
                        else:
                            currRow.append(1)
                    elif seat == "none":
                        currRow.append(3)
                    else:
                        currRow.append(0)       
                    
                seatStatus.append(currRow)

        print(seatStatus)
        self.disp(seatStatus) # calls on the display function to display the seating

        for i in range(len(seats[0])):
            totalSeats.append(seats[0][i]+seats[1][i])   

        return seatStatus

    # books a seat in a screen at a specific time (turning it to false)
    def bookSeat(self, time, row, coloumn, screen):
        row = int(row)
        coloumn = int(coloumn)
        seatData = self.seatInfo(time, screen)
        seats = []
        for key in seatData.keys():
            seats = seatData[key]["seats"]
            print(seats)
            if int(seats[coloumn])-1 >= row:
                ref = db.reference(f"/times/{self.timeSlots[time]}/{time}/{screen}/{key}/available/{row}")
                state = ref.child(f"{coloumn}").get()

                ref.update({f"{coloumn}":"False"})

                print(ref.get())
                break
            row-=int(seats[coloumn])
    
    # function that adds points to a specific user using their username and password
    def addPoints(self, username, password):
        users = self.usersRef.get()
        for key in users.keys():
            if username == users[key]["username"]:
                if password == users[key]["password"]:
                    oldPoints = users[key]["points"]
                    self.usersRef.child(key).update({"points": oldPoints + self.prizePoints})
                    print(self.usersRef.child(key).get())

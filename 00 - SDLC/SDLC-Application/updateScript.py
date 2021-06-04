import reference
from firebase_admin import db
import hashlib

class update():
    def __init__(self):
        self.usersRef = db.reference("/users")
        self.timeRef = db.reference("/times")
        self.screenRef = db.reference("screens")
        self.startingPoints = 10
        self.prizePoints = 5
        self.timeSlots = {
            "09:00":"1morning",
            "10:00":"1morning",
            "13:00":"2afternoon",
            "15:00":"2afternoon",
            "20:00":"3evening"
        }
    
    def getUsers(self):
        users = self.usersRef.get()
        usernames = []
        for keys in users.keys():
            usernames.append(users[keys]["username"])
        return usernames

    def addUser(self, newUsername, newPassword, creditCard, userEmail):
        try:
            users = self.getUsers()
            if newUsername in users:
                return "Account already exists"

            creditHash = hashlib.sha256(str(creditCard).encode()).hexdigest()
            points = self.startingPoints
            newUserData = {
                "username": newUsername,
                "password": newPassword,
                "points": points,
                "credit-card-hash": creditHash,
                "email": userEmail
            }
            self.usersRef.push(newUserData)
            return "Account added to the database"
        
        except:
            return "An error has occured. Please try again at a later time"

    def checkUser(self, username, password):
        users = self.usersRef.get()
        for key in users.keys():
            if username == users[key]["username"]:
                if password == users[key]["password"]:
                    print("Successful")
                    return True

        print("Not Successful, Try Again")
        return False

    def disp(self, seats):
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                out = seats[y][x]
                if out == 3:
                    out = " "
                print(out, end = " ")
            print()

    def seatInfo(self,time,screen):
        times = self.timeRef.get()

        possibleTimes = self.timeSlots.keys()
        if time not in possibleTimes:
            return "This time slot does not exist"
        
        seatData = times[self.timeSlots[time]][time][int(screen)]
        return seatData

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
        self.disp(seatStatus)

        for i in range(len(seats[0])):
            totalSeats.append(seats[0][i]+seats[1][i])   

        return seatStatus

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
        
    def addPoints(self, username, password):
        users = self.usersRef.get()
        for key in users.keys():
            if username == users[key]["username"]:
                if password == users[key]["password"]:
                    oldPoints = users[key]["points"]
                    self.usersRef.child(key).update({"points": oldPoints + self.prizePoints})
                    print(self.usersRef.child(key).get())
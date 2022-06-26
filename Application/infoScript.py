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


from reference import refer # imports the reference script in the directory 
from firebase_admin import db # imports the firebase library

# creates a class called showinfo (requires a set of the data)
class showInfo(set):
    # function that runs when the class is called (or when the class is iniatilized)
    def __init__(self, set):
        self.screens = set['screens']
        self.users = set['users']
        self.times = set['times']

    # function that returns the info about the screens (movies)
    def screen(self):
        screens = self.screens
        print(screens)
        outScreen = screens
        for i in outScreen:
            print(i) # prints the times
        return outScreen

    # function returns the info about the users as an array
    def user(self):
        users = self.users
        outUser = []
        for i in range(len(users)):
            outUser.append(users[str(i)])
        print(outUser) # prints list of users
        return outUser

    # function that returns info about the showing times of all the movies as a list
    def time(self):
        times = self.times
        print("\nTimes:\n")
        timeList = []
        for i in times:
            for j in times[i]:
                print(j) # prints the times 
                timeList.append(j)
        return timeList

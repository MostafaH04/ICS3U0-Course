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


from reference import refer
from firebase_admin import db

class showInfo(set):
    def __init__(self, set):
        self.screens = set['screens']
        self.users = set['users']
        self.times = set['times']

    def screen(self):
        screens = self.screens
        print(screens)
        outScreen = screens
        for i in outScreen:
            print(i)
        return outScreen

    def user(self):
        users = self.users
        outUser = []
        for i in range(len(users)):
            outUser.append(users[str(i)])
        print(outUser)
        return outUser

    def time(self):
        times = self.times
        print("\nTimes:\n")
        timeList = []
        for i in times:
            for j in times[i]:
                print(j)
                timeList.append(j)
        return timeList

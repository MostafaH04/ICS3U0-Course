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
        for i in times:
            print(i)
            for j in times[i]:
                print(f"{j}:")
                for k in times[i][j]:
                    print(f"Screen {int(k)+1}")
                    for l in times[i][j][k]:
                        print(l)
                        print(times[i][j][k][l]['seats'])
                        print("\n")
        return times
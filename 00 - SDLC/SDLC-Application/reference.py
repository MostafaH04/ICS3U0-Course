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

# imports firebase functions classes from firebase library
from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db # db stands for database

# sets the creditials certificate to the json file downloaded from firebase (SDLCkey.json)
cred = credentials.Certificate('SDLCkey.json')
# Istablishes a connection with the database using the initialize_app method, using the downloaded json certificate, and the link to the database
app = initialize_app(cred, {
	'databaseURL':'https://test-4f163-default-rtdb.firebaseio.com/'
	})

# sets a variable that references the database
ref = db.reference("/")

def refer(): return ref # a 1 line function that returns the reference (since the connection cannot be instablished mutliple times)
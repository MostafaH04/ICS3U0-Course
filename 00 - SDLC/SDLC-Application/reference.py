from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db

cred = credentials.Certificate('SDLCkey.json')
app = initialize_app(cred, {
	'databaseURL':'https://test-4f163-default-rtdb.firebaseio.com/',
	'storageBucket': "test-4f163.appspot.com"
	})

ref = db.reference("/")

def refer(): return ref
def application(): return app
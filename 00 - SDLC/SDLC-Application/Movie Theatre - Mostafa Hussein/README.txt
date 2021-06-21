
Installations:
1. Firebase adminstrator
Summary:
This is used to manage the backend of the program, storing and managing information on the database that is hosted on firebase,
using the free spark subscription. Firebase it self has many features, allowing backend python, javascript, node.js developers along with oher developers
to easily launch their web applications or mobile apps, along with an easy to access and manage realtime database, also permiting users to developers to
implement google authentication (using google accounts to sign in) in their applications, and makes it really easy to implement machine learning solutions
to these applications. These features are the main reasons I used firebase, as it offers a lot of easy to use functionallities, and allows for upgradability
possibly being able to implement google authentication or machine learning to my application in the future. Besides that, it was a great learning oppurtunity
to explore this platform that has been gaining a lot of attraction by developers for the past years.

Possible Replacements:
Simply, SQL is a great replacement for firebase, however firebase's features and how easy it is to use made a much better option for me.

Pip cmd:
In command line type: pip install firebase-admin
- This installs the firebase admin library

2. Pygame
Summary:
Pygame is a python library that allows developers to easily develop 2D games using python, providing countless graphical features. The reason I went with
pygame is, it allows me to personally personalize the look of the application as much as I would like, allowing me to implement some animations such as the
movies sliding when changing pages. This of course could be added upon adding a lot more animations in the future. 

Possible Replacements:
Tkinter:
Tkinter is a great replacement as it makes it much easier to make GUI applications, however it does not allow as much creativity and input when it comes to graphics
so I decided to go with pygame instead since I wanted to expirment with the idea of having animations. Another possibility was using Figma to develop the GUI outline
for the Tkinter pages (Figma is a tool used by developers that makes it easy to create amazing front end designs), this would be great, but to do so I must use third 
party scripts and again it wouldnt allow me to configure stuff as much.

Pip cmd:
In command line type: pip install pygame
- This installs the pygame library

3. Hashlib
Summary:
During the emerging technology presentation, I personally discussed encryption used in blockchain, one of which is Hash function, often being the SHA256 hash funtion,
which converts the input to a string of bits that is 256 bits long. Now there is a python library that offers this functionality called Hash lib, and in efforts of
making the application as close to how similar applications in the real world, I am using this method of encryption to encrypt the credit card number inputed by the user.
To do so, I am using this Hashlib, which offers me the SHA256 hash function (irreversable/ hard to crack).

Possible Replacements:
There are a lot of diffferent methods of encrypt information as cryptography is a huge and interesting feild, with different possible ways to hide and ecncrypt information,
however to test out what I discussed in my emergying technology presentation, I felt like using the SHA256 Hash function would be the most interesting thing to do,
that would help me learn more about the function it self.

Pip cmd:
In command line type: pip install hashlib
- Installs the Hashlib library
_______________________________________________________________________________________________________________________________________________________________________________________

Accessing the Database:
The database requires me to share access to the firebase project with any account that wants to access / view the database or other things on it 
(such as the firebase storage that I use to store images on the cloud and link them in the database [for upgradability in the future (to not rely on having images stored locally
as movies sometimes change)]).

Anyhow, the link to the database is: https://test-4f163-default-rtdb.firebaseio.com/
If accessing this is not possible, check the information.json file, which is what is used to reset the database it self, so it is a good method of seeing what is on the database 
it self.

NOTE: Database is set to be temporary, and will stop working on July 1st, it is possible to extend this duration for free, however I will only be using this specific data base for
this application until the end of the Quadmester.

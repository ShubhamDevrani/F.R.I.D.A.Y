import sys
from Body.Speak import Speak
from Body.Listen import Listen

def Password():

    password = "hello world"

    while True:

        Pass = Listen()

        if len(Pass) < 1:
            print("No input of Password")

        elif Pass == password:
            Speak("Password Confirmed.")
            break
        
        else:
            Speak("Incorrect Password")

#Password()
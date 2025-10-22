import datetime
from Body.Speak import Speak

def Wish_Me():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        Speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon Sir")

    else:
        Speak("Good Evening Sir")

#Wish_Me()

def Tell_Day():
    
    day = datetime.datetime.today().weekday() + 1
    Days = {
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thrusday',
                5:'Friday',
                6:'Saturday',
                7:'Sunday'
            }
    
    if day in Days.keys():
        day_of_the_week = Days[day]
        Speak("The day is " + day_of_the_week)

#Tell_Day()
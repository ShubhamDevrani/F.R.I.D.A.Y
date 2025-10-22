import os
import sys
import requests
import datetime
import webbrowser
import pyjokes
import pyautogui
from time import sleep

from Body.Listen import Listen
from Body.Speak import Speak
from Brain.AI_Brain import ReplyBrain
from Brain.Gemini import Gemini

print("\n\n >>  Starting F.R.I.D.A.Y : Wait for some moment")

from Features.Wish import *
from Features.Spotify import *
from Features.WhatsApp import *
from Features.Clap import Tester
from Features.Open import OpenExe
from Features.Password import Password
from Features.Volume import Volume
from Features.PhotoClick import Photo
from Features.HowToDo import HowToDo
from Features.Wikipedia import Wikipedia
from Features.Youtube import YoutubeSearch
from Features.Notepad import NotepadWrite
from FaceRecognition.Face_Recognition import Face_Recognition

print("Module Imported")

print("All Features Loaded!")

def Friday():
    
    Speak("Welcome Sir, Great to see you here.")
    print("F.R.I.D.A.Y is now Online.")
    Speak("Allow me to introduce myself. I am Friday, A virtual Artificial Intelligence, and I am here to assist you with variety of tasks as best as I can, for 24 hours a day and 7 days a week.")
    Speak("System is now fully operationable.")

    while True:

        Data = Listen()
        Data = str(Data)

        if len(Data) < 3:
            pass

        elif 'open chrome' in Data or 'open google' in Data:
            Speak("Opening Chrome sir")
            Path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(Path)
            sleep(2)
            Speak("Chrome Opened")

        elif 'open incognito' in Data:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif 'open history' in Data:
            pyautogui.hotkey('ctrl', 'h')
        elif 'open downloads' in Data:
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in Data:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in Data:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'new tab' in Data:
            pyautogui.hotkey('ctrl', 't')
            sleep(2)
            Speak("New tab opened")
        elif 'close tab' in Data:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close chrome' in Data or 'close google' in Data:
            os.system("taskkill /f /im chrome.exe")
            
        elif 'search' in Data and 'youtube' in Data:
            YoutubeSearch(Data)

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")

        elif 'close youtube' in Data:
            os.system("taskkill /f /im msedge.exe")

        elif 'open facebook' in Data:
            Speak("Opening Facebook Sir")
            webbrowser.open("www.facebook.com")
            sleep(3)
            Speak("Facebook opened.")

        elif 'close facebook' in Data:
            os.system("taskkill /f /im msedge.exe")

        elif 'open whatsapp' in Data:
            Speak("Opening Whatsapp Sir")
            webbrowser.open("web.whatsapp.com")
            sleep(3)
            Speak("Whatsapp opened.")

        elif 'open get into pc' in Data:
            Speak("Opening Getintopc Sir")
            webbrowser.open("www.getintopc.com")
            sleep(3)
            Speak("Getintopc opened.")

        elif 'notepad' in Data and 'write' in Data:
            Speak("Opening Notepad Sir")
            NotepadWrite(Data)

        elif 'open notepad' in Data:
            Speak("Opening Notepad Sir")
            Path = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(Path)
            sleep(2)
            Speak("Notepad opened.")

        elif 'close notepad' in Data:
            os.system("taskkill /f /im notepad.exe")

        elif 'open cmd' in Data or 'open command prompt' in Data:
            Speak("Opening CMD sir")
            Path = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(Path)
            sleep(2)
            Speak("CMD Opened.")

        elif 'close cmd' in Data or 'close command prompt' in Data:
            os.system("taskkill /f /im cmd.exe")

        elif 'open control panel' in Data:
            Speak("Opening Control Panel")
            Path = "C:\\Windows\\System32\\control.exe"
            os.startfile(Path)
            sleep(2)
            Speak("Control Panel Opened")

        elif 'open calculator' in Data:
            Speak("Opening Calculator")
            Path = "C:\\Windows\\System32\\calc.exe"
            os.startfile(Path)
            sleep(2)
            Speak("Calculator Opened")
        
        elif "open" in Data or "launch" in Data or "start" in Data or "visit" in Data:
            Reply = OpenExe(Data)
            sleep(2)
            Speak("Your Task has been executed.")

################################################################################################################################################

        elif "click photo" in Data or "click a photo" in Data or 'take selfie' in Data or 'take photo' in Data:
            Photo()
            
        elif 'activate how to do' in Data:
            HowToDo()

        elif 'wikipedia' in Data:
            Wikipedia(Data)
                                    
        elif 'song please' in Data or 'play some song' in Data or 'could you play some song' in Data or 'play song' in Data:
            Spotify()

        elif "pause song" in Data or 'pause music' in Data or 'stop song' in Data or 'stop music' in Data:
            SpotifyPause()

        elif "send" in Data and "message" in Data:
            try:
                WhatsAppMessage(Data)
            except Exception as e:
                print(e)

        elif "video" in Data and "call" in Data:
            WhatsAppVideoCall(Data)
            sys.exit()

        elif 'joke' in Data:
            joke = pyjokes.get_joke()
            Speak("Sure Master.\n" + joke)

###################################################################################################################################################

        elif "take" in Data and "screenshot" in Data:
            Speak('Tell me a name for the file')
            name = input("Enter name : ")
            Speak("Taking screenshot in 3 seconds.")
            sleep(3)
            img = pyautogui.screenshot() 
            img.save(f"{name}.png") 
            Speak("Screenshot saved.")

        elif "ip address" in Data:
            Speak("Checking....")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                Speak("Your ip adress is : " + ipAdd)
            except Exception as e:
                Speak("Network is weak, please try again some time later")

        elif "increase volume" in Data or 'volume up' in Data:
            for i in range(0,10):
                pyautogui.press("volumeup")

        elif "decrease volume" in Data or 'volume down' in Data:
            for i in range(0,10):
                pyautogui.press("volumedown")
            
        elif 'volume' in Data:
            Volume(Data)

        elif 'close it' in Data:
            pyautogui.hotkey('alt','f4')

        elif "close" in Data:
            Speak("Closing....")
            pyautogui.click(x=1887, y=19)  

        elif "scroll down" in Data:
            pyautogui.scroll(1000)

        elif "the time" in Data:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"The time is {Time}")     

        elif 'clear' in Data and 'notification' in Data:
            Speak("Sure Master")
            pyautogui.hotkey('win','n')
            sleep(2)
            pyautogui.press('tab')
            sleep(0.5)
            pyautogui.press('enter')
            sleep(1)
            pyautogui.hotkey('win','n')
            Speak("Notification Cleared")

        elif "shutdown system" in Data or 'shutdown the system' in Data:
            Speak("OK Sir shuting down the system in 5 seconds.....")
            os.system("shutdown /s /t 5")                   #[/t 5 --> after 5s system will shutdown]

        elif "restart the system" in Data:
            Speak("OK Sir restarting the system in 5 seconds.....")
            os.system("shutdown /r /t 5")                   #[/r --> for restart]

###################################################################################################################################################

        elif "thank you" in Data or "thanks" in Data:
            Speak("Its my pleasure to help you.")
        else:
            try:
                try:
                    Reply = ReplyBrain(Data)
                    Speak(Reply)
                except:
                    Reply = Gemini(Data)
                    Speak(Reply)

            except Exception as e:
                print("\n\nAPI KEY EXPIRE Or SOME ERROR OCCURE....\n")
                print(e)

def Main():
    
    Wish_Me()
    Tell_Day()
    
    # print("Detecting Face....")
    # Face_Recognition()
    # Speak("Face Detected.")
   
    # print("Waitiing for detecting Clap...")
    # query = Tester()

    #if "True-Mic" in query:

    Speak("Password Required for Authorization.")
    Password()
    Speak("All Initialization is completed.")

    Friday()

    # else:
    #     pass

Main()

#Friday()
import os
import pyautogui
from time import sleep
from Body.Listen import Listen
from Body.Speak import Speak

def Spotify():

    Speak('Sir which song should i play...')
    Song = str(Listen())
    #Song = input("Enter the song : ")
    
    try:
        os.startfile("C:\\Users\\Hello World\\AppData\\Roaming\\Spotify\\Spotify.exe")
    except:
        #os.startfile("C:\\Users\\Master SPSG\\AppData\\Roaming\\Spotify\\Spotify.exe")
        os.startfile("C:\\Users\\The Master SPSG\\AppData\\Roaming\\Spotify\\Spotify.exe")

    sleep(3.5)
    pyautogui.hotkey('ctrl', 'k')
    sleep(0.5)
    pyautogui.write(Song)
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    
    pyautogui.click(x=1775, y=21)

def SpotifyPause():

    try:
        os.startfile("C:\\Users\\Hello World\\AppData\\Roaming\\Spotify\\Spotify.exe")
    except:
        os.startfile("C:\\Users\\The Master SPSG\\AppData\\Roaming\\Spotify\\Spotify.exe")
        #os.startfile("C:\\Users\\Master SPSG\\AppData\\Roaming\\Spotify\\Spotify.exe")
        
    sleep(1)
    pyautogui.hotkey("space")
    sleep(1)
    pyautogui.click(x=1775, y=21)

#Spotify()
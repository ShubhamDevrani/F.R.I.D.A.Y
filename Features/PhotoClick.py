import pyautogui
from time import sleep
from pyautogui import click

from Body.Speak import Speak

def Photo():
    Name = input("Enter your Name: ")

    pyautogui.press('win')
    sleep(0.5)
    
    pyautogui.write('Camera')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(3)

    Speak('1, 2, 3' + '\nSay Cheeze')

    pyautogui.press('space')

    Speak("Welcome " + Name)
    sleep(2)
    pyautogui.hotkey('alt', 'f4')

#Photo()
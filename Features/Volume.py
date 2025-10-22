import pyautogui
from time import sleep
from Body.Speak import Speak

def Volume(Data):

    pyautogui.click()
    sleep(2)

    if '10' in Data:
        pyautogui.click()
        Speak("Volume Level 10")

    elif '20' in Data:
        pyautogui.click()
        Speak("Volume Level 20")

    elif '30' in Data:
        pyautogui.click()
        Speak("Volume Level 30")

    elif '40' in Data:
        pyautogui.click()
        Speak("Volume Level 40")

    elif '50' in Data:
        pyautogui.click()
        Speak("Volume Level 50")

    elif '60' in Data:
        pyautogui.click()
        Speak("Volume Level 60")

    elif '70' in Data:
        pyautogui.click()
        Speak("Volume Level 70")

    elif '80' in Data:
        pyautogui.click()
        Speak("Volume Level 80")

    elif '90' in Data:
        pyautogui.click()
        Speak("Volume Level 90")

    elif 'full' in Data or 'max' in Data:
        pyautogui.click()
        Speak("Volume Level max")

    elif 'mute' in Data or 'unmute' in Data:
        pyautogui.click()
        Speak("Task has been executed")
    
    pyautogui.click()

#Volume(Data = "jarvis set volume to 10")
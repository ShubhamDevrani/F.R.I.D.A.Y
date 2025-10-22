import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    
    Query = str(Query).lower()
    Query = Query.replace("friday","")
    
    if "visit" in Query:
        Name_of_Web = Query.replace("visit ","")
        Link = f"https://web.{Name_of_Web}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Name_of_Web = Query.replace("launch ","")
        Link = f"https://www.{Name_of_Web}.com"
        webbrowser.open(Link)
        return True

    elif "start" in Query:

        Name_of_App = Query.replace("start","")

        pyautogui.press('win')
        sleep(1)
        pyautogui.write(Name_of_App)
        sleep(1)
        pyautogui.press('enter')
        sleep(0.5)
        return True

    elif "open" in Query:

        Name_of_App = Query.replace("open","")

        pyautogui.press('win')
        sleep(1)
        pyautogui.write(Name_of_App)
        sleep(1)
        pyautogui.press('enter')
        sleep(0.5)

        return True

# Name = input("Enter : ")        
# OpenExe(Name)
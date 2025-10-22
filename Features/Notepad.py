import os
import pyautogui
from time import sleep

def NotepadWrite(Data):
    
    Path = 'C:\\Windows\\System32\\notepad.exe'
    os.startfile(Path)
    write = Data.replace("friday open notepad and write","")
    write = write.replace("ok friday","")
    write = write.replace("open notepad and write","")
    write = write.replace("write in notepad that","")
    write = write.replace("on notepad write","")
    write = write.replace("in notepad write","")
    sleep(1)
    pyautogui.write(write, interval = 0.05)
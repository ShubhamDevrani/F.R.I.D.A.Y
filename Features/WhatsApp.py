import pathlib
from time import sleep
from pyautogui import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from Body.Speak import Speak
from Body.Listen import Listen

def WhatsAppOpen():

    url = "https://web.whatsapp.com/"
    Path = "DataBase\\Chrome\\Chrome Driver\\chromedriver.exe"
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/124.0.6367.92 Safari/537.2"
    user_data_dir = pathlib.Path().absolute()

    services = Service(Path)
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument(f"user-data-dir={user_data_dir}\\DataBase\\Chrome\\Chrome Data\\chromedata whatsapp")

    global driver
    driver = webdriver.Chrome(service = services, options = chrome_options)
    driver.minimize_window()
    driver.get(url=url)
    
    Speak("Opening Whatsapp Sir.")
    print("Wait for a momemt.")
    driver.maximize_window()
    #sleep(10000)
    WebOpenCheck()

def WebOpenCheck():

    Xpathlogin = "/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/span/div"
    Xpathafterloginbutton = "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[2]/button[1]"
    while True:
        try:
            driver.find_element(by=By.XPATH, value=Xpathlogin)
            Speak("Please login your Whatsapp first...")
            #print("Please login first...")
            driver.maximize_window()
            try:
                driver.find_element(by=By.XPATH, value=Xpathafterloginbutton)
                break
            except:
                pass
        except:
            try:
                driver.find_element(by=By.XPATH, value=Xpathafterloginbutton)
                break
            except:
                pass
    driver.minimize_window()


def WhatsAppMessage(Data):

    WhatsAppOpen()
    
    Data = Data.replace("friday send message to ","")
    Data = Data.replace("send message to ","")
    
    Query1 = Data
    Xpathsearch = "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/p"
    driver.find_element(by=By.XPATH, value=Xpathsearch).send_keys(Query1)
    driver.find_element(by=By.XPATH, value=Xpathsearch).send_keys(Keys.ENTER)
    
    Speak("OK sir, tell your message...")
    Query2 = Listen()
    #Query2 = input("Enter your messaage : ")
    driver.maximize_window()

    Xpath2 = "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p"
    driver.find_element(by=By.XPATH, value=Xpath2).send_keys(Query2)
    
    Xpath3 = "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[2]/button"
    driver.find_element(by=By.XPATH, value=Xpath3).click()

    Speak("Your message is sent.")
    sleep(3)
    driver.quit()
    Speak("WhatsApp is closed...")


def WhatsAppVideoCall(Data):
    
    Data = Data.replace("friday","")
    Data = Data.replace("video call","")

    hotkey("win")
    sleep(1)
    write("whatsapp")
    sleep(1)
    hotkey("enter")
    sleep(5)
    click()
    sleep(1)
    write(Data)
    sleep(1)
    click()
    sleep(1)
    click()

#WhatsAppMessage("friday send message to 9045118079")
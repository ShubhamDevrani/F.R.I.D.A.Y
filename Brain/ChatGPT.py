import pathlib
import warnings
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options                                                 # Used in giving feature to chrome & bypassing the web security
from selenium.webdriver.chrome.service import Service                                                 # Used for handling chromedriver
from selenium.webdriver.common.by import By                                                           # For Xpath (driver kis adhar par choose kar rha hai)

warnings.simplefilter("ignore")

Script_Directory = pathlib.Path().absolute()                                                          # Taking out the current Directory location 
#print(Script_Directory)
'''
from webdriver_manager.chrome import ChromeDriverManager                                              # Importing chromedriver
service = Service(ChromeDriverManager().install())                                                    # Service() providing the path of chromedriver to the current folder
'''

Path = "D:\\Apps\\Google Chrome\\Chrome Driver\\chromedriver.exe"
service = Service(Path)

url = "https://flowgpt.com/chat"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"

chrome_options = Options()                                    
chrome_options.add_argument("--headless=new")                                                         # Chrome work in backend and do not open.       
chrome_options.add_argument(f"user-agent={user_agent}")                                               # Using Options() and adding user_agent in it as agruement entering in the webpage as a user not as a bot.

# Remembering chrome from where it closed
chrome_options.add_argument("--profile-directory=Default")                                            # For chorme data saving -- includes Pathlib
chrome_options.add_argument(f"user-data-dir={Script_Directory}\\DataBase\\Chrome\\chromedata")        # Pathlib -- Giving the location so that chrome save data and chrome opens from where it was closed.

driver = webdriver.Chrome(service=service, options=chrome_options)                                    # Giving chromedriver all arguements for entering in website
driver.maximize_window()                                                                              # Maximize the chrome
driver.get(url=url)

ChatNumber = 3                                                                                        # For ResultScrapper & UpcomingChatNo

def UpcomingChatNo():
    global ChatNumber
    for i in range(3,1000,2):                                                                         # Taking out odd no. starting from 3 for resultscrapping as chatgpt text xpath is on odd numbers.
        try:
            ChatNumber = str(i)                                                                       # Converting integer into string for Xpath
            Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
            driver.find_element(by=By.XPATH, value=Xpath)                                             # Finding the element through Xpath if got then checking for new i.

        except:
            ChatNumber = i                                                                            # If i(odd) xpath did not found then it means that the initial chat will start that i now and giving value of i to chatnumber then resultscrapping function will do the rest of the thing
            print("The next Chatnumber is : ",i)
            break

def WebOpenCheck():
    Xpath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea"
    while True:
        try:
            driver.find_element(by=By.XPATH, value=Xpath)                                             # Find the element and checking that it is visible if visible then website is fully loaded then break the statement.
            break

        except:
            pass

def SendMessage(Query):

    Xpath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea"
    driver.find_element(by=By.XPATH, value=Xpath).send_keys(Query)                                    # Sending text into textarea
    sleep (0.5)
    Xpath2 = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button"
    driver.find_element(by=By.XPATH, value=Xpath2).click()                                            # Click on send button of chatgpt 

def ResultScrapper():
    global ChatNumber                                                                                 # Using the ChatNumber inside the function which is declared outside of function using global.
    ChatNumber = str(ChatNumber)                                                                      # Converting interger into string for Xpath.
    
    Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"

    Text = driver.find_element(by=By.XPATH, value=Xpath).text                                         # Coping the text generated by chatgpt
    #print(Text)
    
    NewChatNumber = int(ChatNumber) + 2                                                               # Converting string into interger and adding for more result scrapping.
    ChatNumber = NewChatNumber
    return Text

def AnswerWait():
    sleep(2)                                                                                          # Because before chatgpt give answer it take some time then xpath will not visible for that movement no answer we will get so sleep for 2 sec 
    Xpath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/button"
    while True:
        try:
            driver.find_element(by=By.XPATH, value=Xpath)                                             # Tab tak find karega jab tak element dikhega or jesehi dikna band ek error ayeaga usko excpet statement sai break karenge.
            
        except:
            break

WebOpenCheck()
UpcomingChatNo()

while True:

    Query = input("Enter your Query : ")                                                              # For Listen Function
    Query = str(Query)                                                                                  
    SendMessage(Query=Query)
    AnswerWait()
    Text = ResultScrapper()
    print(Text)
    print("")
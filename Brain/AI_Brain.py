import openai
from dotenv import load_dotenv

# API Key :

fileopen = open("DataBase\\Keys\\API.txt","r")
API = fileopen.read()
fileopen.close()

# Code :

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):

    FileLog = open("Data\\AI_Brain\\Chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nFriday : '

    response = completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)

    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nFriday: {answer}"

    FileLog = open("Data\\AI_Brain\\Chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    
    return answer

'''
while True:
    repeat = input("Enter : ")
    print("\n",ReplyBrain(repeat),"\n \n")
'''
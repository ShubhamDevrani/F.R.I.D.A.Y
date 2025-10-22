import speech_recognition as sr
from googletrans import Translator

def Listen_1():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)    # [ 8 ] is closing timer.
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
    except:
        return ""

    query = str(query).lower()
    print("")
    print("YOU : ",query)

    return query
# Listen_1()

def TranslationHinToEng(Text):

    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    return data

def Listen():
    query = Listen_1()
    data = TranslationHinToEng(query)
    return data
#print(Listen())
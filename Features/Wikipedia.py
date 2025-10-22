import wikipedia
from Body.Speak import Speak

def Wikipedia(Data):

    Speak("Sure Sir\n" + "Searching Wikipedia...")

    Data = Data.replace("wikipedia", "")
    Data = Data.replace("friday", "")
    Data = Data.replace("about","")
            
    results = wikipedia.summary(Data, sentences = 2)
    Speak("According to Wikipedia\n" + results)
from Body.Speak import Speak
from Body.Listen import Listen
from pywikihow import search_wikihow

def HowToDo():
    Speak("How to Do mode activated. Please tell me what you want to learn.")
    
    Mode = Listen()
    max_results = 1
    HOW = search_wikihow(Mode, max_results)
    
    if HOW:
        Speak(HOW[0].summary)
    else:
        Speak("Sorry, I couldn't find any information on that topic.")

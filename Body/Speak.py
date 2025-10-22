import pyttsx3

def Speak(Text):

    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)          # [0] = male voice, [1] = female voice
    engine.setProperty('rate', 190)                     # 190 is voice speed

    print("")
    print("AI : ",Text)
    print("")
    
    engine.say(Text)
    engine.runAndWait()

#Speak("hello how are you arshit nice to meet you")
# pip install pyttsx3 ; this works offline
import pyttsx3

def text_to_Speech(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init()    #  ----------->>  object for pyttsx3 class

for voice in engine.getProperty("voices"):   #  ------->>  To check the number of voices in system
    print(voice)
    
voices = engine.getProperty("voices")    
engine.setProperty("voice", voices[0].id)   #  --------->>  Setting up any voice

text = input("Enter your text : ")
text_to_Speech(text)
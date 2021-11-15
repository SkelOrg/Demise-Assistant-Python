from os import name
import webbrowser
import pyttsx3
from datetime import *

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def getTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def create_note():
    text = input("Enter your note: ")
    file = open("notes.txt", "a") 
    file.write(f"{getTime()} - {text}\n")
    file.close()

    print(f"Your note has been created at {getTime()}")
    text_to_speech("Note created.")
    
def getWebsiteTitle(url):
    # Get the url's website name and return it
    # for example: https://github.com returns github
    # Note: This should also work for 'http://'
    return url.split("//")[-1].split(".")[0]

def openUrl(url):
    webbrowser.open_new_tab(url)
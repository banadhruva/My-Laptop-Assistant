import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import time 




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print((voices[0].id))  #for details of voice
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>12 and hour<18 :
        speak("Good Afternoon")
    else :
        speak("Good Evening!")
       
    speak("Namaskaram ! Hey there, what can i do for you")


def takeCommand(): 
     #takes microphone input & returns a string 
    
    r=sr.Recognizer() 
    with sr.Microphone() as source :
        print("Listening.....")
        r.pause_threshold = 1   # seconds of non-speaking audio before a phrase is considered complete
        audio= r.listen(source)
    
    try:
        print("Recognizing....") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query

if __name__=="__main__" :
    wishme()
    query= takeCommand().lower()
        

    if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences = 5)
            speak("According to wikipedia")
            speak(results)
            print(results)

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")
        
    elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
           speak("Which song would you like to listen")
           song_name = takeCommand()
           os.system("spotify")
           time.sleep(5)
           pyautogui.hotkey('ctrl','l')
           pyautogui.write(song_name,interval=0.5)
           for key in['enter', 'pagedown','tab','enter','enter']:
               time.sleep(2)
               pyautogui.press(key)
           print(song_name)
           

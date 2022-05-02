import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys

emailDictionary = {
    "jayesh mahale" : "mahalej103@gmail.com",
    "jayesh patil" : "jp7470484@gmail.com"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


@staticmethod
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you!")

def takeCommand():
    # it take microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"
    return query
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    with open("D:\\Password.txt") as f:
        information = f.read()

    server.login('mrprogramer18@gmail.com', information)
    server.sendmail('mrprogramer18@gmail.com', to, content)


if __name__ == "__main__":
    # speak("Jayesh is good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing takes based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            songs_len = len(songs) - 1
            print(songs)
            randNumber = random.randint(0, songs_len)
            print(randNumber)
        
            os.startfile(os.path.join(music_dir,songs[randNumber]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\jp747\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()

                if "jayesh patil" in query:    
                    to = emailDictionary['jayesh patil']
                elif "jayesh mahale" in query:
                    to = emailDictionary['jayesh mahale']
                else:
                    print("Email not found!, Please give valid user name")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not abble to send")
        
        elif "exit jarvis" in query:
            sys.exit()

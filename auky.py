import pyttsx3      # python text tom speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')    # import microsoft voices api
voices = engine.getProperty('voices')
# print(voices[0].id)

# 0 for david and 1 for zira (microsoft inbuilt two voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()     # it is a fuction | speech function |


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Auky. Ready to help you!")


def takeCommand():
    '''
    It takes microphone input from user and return string output
    '''
    r = sr.Recognizer()   # Recognizer class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        # speak("Say that again please..,")
        return "None"  # none string if any problem
    return query


def sendEmail(to, content):        # by using smtp lib + enable less secure apps in google
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs\\Pahadi'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'open VS code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'send email to []' in query:
            try:
                speak("What shoul I say!")
                takeCommand()
                to = "yanik.kumar@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry I'm unable to send email currently!")

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "PRIYANSH"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        query = None
    return query

speak("Initializing Jarvis...")
print("Initializing Jarvis...")
#wishMe()
#query = takeCommand()
query = "hey jarvis open file"
query = query.lower()


if 'wikipedia' in query:
    speak('Searching wikipedia..')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)

elif 'open youtube' in query:
    #webbrowser.open("youtube.com")
    speak('Opening Youtube..')
    url = "youtube.com"
    #webbrowser.get(using='google-chrome').open(url,new=new)
    chrome_path = 'C:///Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open google' in query:
    url = "google.com"
    chrome_path = 'C:///Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query:
    songs_dir = "c:\\Users\\ajay\\Downloads"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir,songs[0]))

elif 'time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")

elif 'open file' in query:
    drive = input('your file is in which drive? ')
    file_dir = drive + ":\\"
    flag = 1
    #file_dir = "F:\\Priyansh\\Python\\Intel AI Course\\dc_to_the_edge\\DC to Edge Course\\Notebooks"
    if os.path.exists(file_dir) == False:
        drive = input('Enter drive again : ')
        file_dir = drive + ":\\"
        if os.path.exists(file_dir) == False:
            flag = 0        
    while flag:
        files = os.listdir(file_dir)
        print("\n",file_dir.center(50),"\n")
        print([(i,files[i]) for i in range(len(files))],"\n")
        folder = int(input('Enter index of folder [-1 to go back & -2 to exit] : '))
        if folder == -1:
            t = file_dir.rfind('\\')
            if os.path.exists(file_dir[:t]):
                file_dir = file_dir[:t]
            else:
                print('Path does not exist, Try again!')
        elif folder == -2:
            flag = 0
        else:
            if os.path.isdir(file_dir+'\\'+files[folder]):
                file_dir += "\\" + files[folder]
            else:
                print('Folder does not exist, Try again')
    if os.path.exists(file_dir):
        files = os.listdir(file_dir)
        print("\n",file_dir.center(50),"\n")
        print([(i,files[i]) for i in range(len(files))],"\n")
        file = int(input('\nwhich file? '))
        os.startfile(os.path.join(file_dir,files[file]))
    else:
        print('Path does not exist..')
    
    

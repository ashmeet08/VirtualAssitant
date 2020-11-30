import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import *

print("Initializing Jatt")

master = "Ashmeet"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak func will speak the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
#this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ master)
    else:
        speak("Good Evening" + master)

    speak("I am Jatt. How may i help you?")
#this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("I am unable to understand that. Say it again please")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('username','password')
    server.sendmail('recipetent mail',to, content)
    server.close()
#Main program starts here

def main():
    speak("Initializing Jatt...")
    wishMe()
    query = takeCommand()

    #logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'google' in query.lower():
        speak('Searching Google....')
        query = query.replace("Google","")
        #results = google.summary(query)
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        #webbrowser.get(chrome_path).open(url: query)
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.get(chrome_path).open("https://google.com/search?q=%s" % query)


    elif 'open outlook' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "outlook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "E:\\Ashmeet\\Download"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[2]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"[master] the time is {strTime}")

    elif 'set alarm' in query.lower():
        now = datetime.datetime.now()
        query = query.replace("set alarm for","")
        # Choose 6PM today as the time the alarm fires.
        # This won't work well if it's after 6PM, though.
        query
        alarm_time = datetime.datetime.combine(now.date(), datetime.time(query))

        # Think of time.sleep() as having the operating system set an alarm for you,
        # and waking you up when the alarm fires.
        time.sleep((alarm_time - now).total_seconds())

        os.system("start BTS_House_Of_Cards.mp3")

    elif 'weather' in query.lower():
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
        
        city_name = input("Enter city name : ") 
        
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        
        # get method of requests module 
        # return response object 
        response = requests.get(complete_url) 
        
        # json method of response object  
        # convert json format data into 
        # python format data 
        x = response.json() 
        
        # Now x contains list of nested dictionaries 
        # Check the value of "cod" key is equal to 
        # "404", means city is found otherwise, 
        # city is not found 
        if x["cod"] != "404": 
        
            # store the value of "main" 
            # key in variable y 
            y = x["main"] 
        
            # store the value corresponding 
            # to the "temp" key of y 
            current_temperature = y["temp"] 
        
            # store the value corresponding 
            # to the "pressure" key of y 
            current_pressure = y["pressure"] 
        
            # store the value corresponding 
            # to the "humidity" key of y 
            current_humidiy = y["humidity"] 
        
            # store the value of "weather" 
            # key in variable z 
            z = x["weather"] 
        
            # store the value corresponding  
            # to the "description" key at  
            # the 0th index of z 
            weather_description = z[0]["description"] 
        
            # print following values 
            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) + 
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n description = " +
                            str(weather_description)) 
            speak(" Temperature (in kelvin unit) = " +
                            str(current_temperature) + 
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n description = " +
                            str(weather_description))
        
        else: 
            print(" City Not Found ") 

    elif 'open code' in query.lower():
        codepath = "C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'email to ' in query.lower():
        try:
            speak("what should I send")
            content = takeCommand()
            to = "recipetent mail"
            sendEmail(to, content)
            speak("Email sent successfully")
        except Exception as e:
            print(e)

main()
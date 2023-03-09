from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition
import requests
import datetime
import os
import pyautogui
import webbrowser
import random
import mixer
import notification
import speedtest
from INTRO import play_gif
play_gif
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate = engine.setProperty("rate",150)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "go to sleep" in query:
            speak("Ok sir , You can call me  anytime")
            break 
        elif "hello" in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "temperature" in query:
            search = "temperature in tunisia"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
            search = "temperature in tunisia"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
        elif "finally sleep" in query:
            speak("Going to sleep,sir")
            exit()
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")
        
        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")
        elif "maximize" in query:
            pyautogui.press("f")
            speak("screen maximised")
        elif "minimize" in query:
            pyautogui.press("f")
            speak("screen minimized")
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()
        elif "close this tab" in query:
            pyautogui.press("ctrl+w")
            
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me  " + remember.read())
        elif "recommend a movie" in query:
            a = (0,1)
            b = random.choice(a)
            drama = ["https://www.netflix.com/watch/20557937?trackId=255824129&tctx=0%2C43%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247312468_titles%2F1%2F%2Fdarma%2F0%2F0%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247312468_titles%2F1%2F%2Fdarma%2F0%2F0%2Cunknown%2C%2Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247312468%7C1%2CtitlesResults%2C20557937%2CVideo%3A20557937","https://www.netflix.com/watch/70060015?trackId=255824129&tctx=0%2C23%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247312468_titles%2F1%2F%2Fdarma%2F0%2F0%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247312468_titles%2F1%2F%2Fdarma%2F0%2F0%2Cunknown%2C%2Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247312468%7C1%2CtitlesResults%2C70060015%2CVideo%3A70060015"]
            comedy =["https://www.netflix.com/watch/70027007?trackId=255824129&tctx=0%2C18%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247208806_titles%2F1%2F%2Fcomdy%2F0%2F0%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247208806_titles%2F1%2F%2Fcomdy%2F0%2F0%2Cunknown%2C%2Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247208806%7C1%2CtitlesResults%2C70027007%2CVideo%3A70027007","https://www.netflix.com/watch/17236928?trackId=255824129&tctx=0%2C16%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247208806_titles%2F1%2F%2Fcomdy%2F0%2F0%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247208806_titles%2F1%2F%2Fcomdy%2F0%2F0%2Cunknown%2C%2Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-247208806%7C1%2CtitlesResults%2C17236928%2CVideo%3A17236928"]
            action =["https://www.netflix.com/watch/80200961?trackId=255824129&tctx=0%2C28%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-246593400_titles%2F1%2F%2Faction%2F0%2F0%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-246593400_titles%2F1%2F%2Faction%2F0%2F0%2Cunknown%2C%2Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-246593400%7C1%2CtitlesResults%2C%2CVideo%3A80200961","https://www.netflix.com/watch/80236390?trackId=255824129&tctx=0%2C1%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-246593400_titles%2F1%2F%2Faction%2F0%2F0%2CNAPA%40%40%7Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-246593400_titles%2F1%2F%2Faction%2F0%2F0%2Cunknown%2C%2Ce14c9a1e-210e-4b61-bbff-2e3a8cae6bae-246593400%7C1%2CtitlesResults%2C80236390%2CVideo%3A80236390"]
            movietype=['action','comedy','drama'] 
            speak("what gener of movie you want to watch Sir")
            speak(movietype)
            speak("chose one Sir Write 1 for action 2 for comedy 3 for drama")
            x = int(input("Write 1 for action 2 for comedy 3 for drama "))
            if x == 1:
                webbrowser.open(action[b])
            elif x ==2:
                webbrowser.open(comedy[b])
            else :
                webbrowser.open(drama[b])
            speak("playing the movie for you ")
        elif "change my mood" in query:
            speak("Playing your favourite songs, sir")
            playlist = ["https://www.youtube.com/watch?v=whH6L9JZS7M","https://www.youtube.com/watch?v=dgUGzcDXm4Y","https://www.youtube.com/watch?v=P_ikNip_tFo"]
            a = (0,1,2) # You can choose any number of songs (I have only choosen 3)
            b = random.choice(a)
            webbrowser.open(playlist[b])
        
        elif "news" in query:
            from NewsRead import latestnews
            latestnews()
        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            Calc(query)
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()
        elif "shut down the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break    
        elif "schedule my day" in query:
            tasks = [] #Empty list 
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takeCommand().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()                        
        elif "show my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 15
                )
        elif "open" in query:   #EASY METHOD
            query = query.replace("open","")
            query = query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")   
        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")
        elif "play a game" in query:
            from game import game_play
            game_play(query)
        elif "screenshot" in query:
                import pyautogui #pip install pyautogui
                im = pyautogui.screenshot()
                im.save("ss.jpg")
        elif "photo shot" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")
        elif "translate" in query:
            from Translator import translategl
            query = query.replace("jarvis","")
            query = query.replace("translate","")
            translategl(query)


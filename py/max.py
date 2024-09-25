import speech_recognizer as sr
import pyttsx3
from GoogleNews import GoogleNews
import pywhatkit
import datetime
import pyautogui as pg
import wikipedia
import webbrowser
import os
import psutil
import time
from tkinter import *
import random
#importnt resource
password = 'Meh@di.08'
fb_pass='I_can_m@ke_The_baD_Girls_gOOd_For_a_WeekEnd_82542'
gmail = 'metalha68@gmail.com'
phone = '01922691942'
email= 'metalha034@gmail.com'
motivation = 'D:\\talha coding\\web design projects\\python\\max\\text files\\motivation.txt'
#speak engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert voice to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('listening, sir')
        r.pause_threshold = 1 #how long mx will hear us
        audio = r.listen(source)
    try:
        print('recognizing....')
        query=r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        speak('didnt get it')
        return 'none'
    return query
#wish goood morning or good evening 
def wish():
    hour = int(datetime.datetime.now().hour)
    if (5<hour<12):
        speak("Good Morning, sir")

    elif (12<hour<19 ):
        speak ("good afternoon, sir")
    else:
        speak ('good evening, Sir')
#log in 
def log_in():
        url='https://chat.openai.com'
        webbrowser.open(url)
        time.sleep(1)
        pg.press("f11")
        pg.moveTo(x = 1829, y=712)
        #opened chat GPT
        time.sleep(20)
        #log_in
        pg.press('tab')
        pg.press('enter')
        time.sleep(10)
        #email
        pg.write(gmail)
        #continue
        pg.press('enter')
        time.sleep(2)
        pg.write(password)
        pg.press('enter')
        
        speak('chatGPT log in succesful')
        time.sleep(10)
        #next_click
        for i in range(3):
            pg.press('enter')
        #chatgpt mission complete
        url='https://www.facebook.com/'
        webbrowser.open(url)
        time.sleep(10)
        #email/phone
        pg.write(phone)
        #passbar
        pg.press('tab')
        time.sleep(2)
        pg.write(fb_pass)
        time.sleep(2)
        pg.press('enter')
        speak('Facebook log in succesful')
        #facebook mission completed
        url='https://www.youtube.com/'
        webbrowser.open(url)
        pg.press('enter')
        time.sleep(10)
        #singn_in
        for i in range(8):
            pg.press('tab')
        pg.press('enter')
        time.sleep(5)
        pg.hotkey('ctrl', 'a')
        pg.press('delete')
        pg.write(email)
        pg.press('enter')
        time.sleep(2)
        pg.write(password)
        pg.press('enter')
        speak('youTube log in succesful')
        #youtube mission completed
        url='https://www.instagram.com/'
        webbrowser.open(url)
        time.sleep(10)
        #continue_withfacebook
        for i in range(3):
             pg.press('tab')
        pg.press('enter')
        speak('Instagram log in succesful')
            #codepen log in 
        url = 'https://codepen.io/login'
        webbrowser.open(url)
        time.sleep(10)
        for i in range(21):
            pg.press('tab')
        pg.press('enter')
        pg.write('metalha68@gmail.com')
        time.sleep(1)
        pg.press('tab')
        pg.write(password)
        pg.press('enter')  
        speak ('codepen log in succesfull')
        replit = 'https://replit.com/login'
        webbrowser.open(replit)
        time.sleep(5)
        for i in range(3):
            pg.press('tab')
            time.sleep(1)
        pg.press('enter')
        time.sleep(5)
       
#history delete
def delete():
    os.startfile('"C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe"')
    time.sleep(2)
  
    pg.press("f11")
   
    pg.moveTo(x = 1829, y=712)
    pg.hotkey('ctrl', 'h')
    for i in range(4):
        time.sleep(1)
        pg.press('tab')
    pg.press('enter')
    pg.press('down')
    pg.press('enter')
    time.sleep(2)
    for i in range(12):
        time.sleep(1)
        pg.press('tab')
    time.sleep(1)
    pg.press('enter')
#motivation
def Motivation():
    lines = open(motivation).read().splitlines()
    lines = random.choice(lines)
    speak(lines)
#whatsapp
def whatsappMsg(name , message):
    url='https://web.whatsapp.com/'
    webbrowser.open(url)
    pg.press(f11)
    pg.moveTo(x = 1829, y=712)
    time.sleep(20)
    # pg.click(x = 125, y = 258) #search
    for i in range(6):
        pg.press('tab')
    pg.write(name)
    time.sleep(1)
    # pg.click(x=212 , y=414) #chat head
    for i in range(2):
        pg.press('tab')
    pg.press('enter')

    pg.write(message)
    time.sleep(1)
    pg.press('enter') #send button
#messener  
#log out
def log_out():
      url='https://www.facebook.com/'
      webbrowser.open(url)
      time.sleep(10)
      pg.click(x=1849, y=41)
      time.sleep(3)
      for i in range(7):
            pg.press('tab')
      pg.press('enter')

#bluetooth
def bluetooth(): 
    pg.click(x=1888, y=1061)#menu
    time.sleep(1)
    pg.click(x=1712, y=983)#bluetooh button
    time.sleep(1)
    pg.click(x=1888, y=1061)#menu
#night light
def nightmode():
    pg.click(x=1888, y=1061)#menu
    time.sleep(1)
    pg.click(x=1836, y=979)#nightmode button
    time.sleep(1)
    pg.click(x=1888, y=1061)#menu
#working setup
def work():

    #time and date
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(time)
    date = datetime.datetime.now().strftime('%d-%B-%Y')
    date = 'Today is' + date 
    speak(date)
    week = datetime.datetime.now().strftime('%A')
    week = 'It is ' + week
    speak(week)
    #motivation
    Motivation()
    #log in 
    log_in()
    #open VS code
    os.startfile('"C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
    pg.press('f11')
    #take_note
    pg.press('win')
    pg.write('stickey') 
    pg.press('enter')
    #open work firendly window made by me
    os.startfile('D:\\talha coding\\web design projects\\index.html')
    pg.press('f11')
    #position tracker
    os.startfile('D:\\talha coding\\web design projects\\python\\position.py')
    #chat_gpt
    url='https://chat.openai.com'
    webbrowser.open(url)
    #playground ai
    url='https://playgroundai.com/canvas/cljx83sjp0knds6010oud1um7'
    webbrowser.open(url)
#news
def news():
    googlenews = GoogleNews()
    speak('Collecting News, sir')
    googlenews.get_news(command)
    googlenews.result()
    a = googlenews.gettext()
    a = a[1:5]
    speak(a) 
#startup
def start_up():
        pg.hotkey('win', 'r')
        pg.hotkey('alt', 'a')
        pg.press('delete')
        pg.write('shell:startup')
        pg.press('enter')
if __name__ == '__main__':
    wish()
    speak('I am Max. Your personal assistant,sir. Tell me how can I help you?')
    while True:
        command = take_command().lower()
        #logic for max
        if 'news' in command:
            news()
        if 'play' in command:
            song = command.replace('play', '')
            print(song)
            speak('playing' + song)
            pywhatkit.playonyt(song)
        elif 'start' in command:
            start_up()
        elif 'login' in command:
            log_in()
        elif 'logout' in command:
            log_out()
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(time)
        elif 'who the hell is' in command:
            person = command.replace('who the hell is', '')
            bio = wikipedia.summary(person, 3)
            print(bio)
            speak(bio)
        elif 'what the hell is' in command:
            things = command.replace('what the hell is', '')
            info = wikipedia.summary(things, 3)
            print(info)
            speak(info)
        elif 'what is my phone number' in command:
            phone = '01521745815'
            speak(phone + 'sir')
        elif 'what is my mail' in command:
            mail = 'metalha68@gmail.com'
            speak(mail + 'sir')
        elif 'who created you' in command:
            name = 'Mehadi Hasan Talha'
            speak(name + 'sir')
        elif 'search' in command:
            ser = command.replace('search', '')
            speak('searching'+ ser + 'sir')
            pywhatkit.search(ser)
        elif 'meta' in command:
            url='https://www.facebook.com/'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        elif 'WhatsApp' in command:
            url='https://web.whatsapp.com/'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        elif 'new pen' in command:
            url='https://codepen.io/pen/'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        elif 'work' in command:
            work()
        elif 'insta' in command:
            url='https://www.instagram.com/'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        
        elif 'telegram' in command:
            url='https://web.telegram.org/k/'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        elif 'type' in command:
            text = command.replace('type', '')
            pg.write(text)
        elif 'GPT' in command:
            url='https://chat.openai.com'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        elif 'add' in command:
            pg.click(x= 1141, y=749)
        elif 'YouTube' in command:
            url='https://www.youtube.com/'
            speak('opening' +'' +'sir')
            webbrowser.open(url)
        elif 'skip' in command:
            pg.click(x=1158, y=143)
        elif 'there' in command:
            speak('always at your service' + 'sir')
            
        elif 'thanks' in command:
            speak('my pleasure' + 'sir')
        elif 'love' in command:
            speak('love is a waste of time. ' + 'sir')
        elif 'how are you' in command:
            speak('I am fine thank you. ' + 'sir')
        elif 'fuck' in command:
            speak('fuck you too' + 'sir')
        elif 'off' in command:
            log_out()
            delete()
            speak('shutting down computer now..'+'sir')
            os.system("shutdown /s")
            time.sleep(10)
            pg.press('enter')
        elif 'restart' in command:
            speak('Restarting the system...'+'sir')
            os.system("shutdown /r")
        elif 'up' in command:
            speak('volume increasing'+'sir')
            pg.press('volumeup')
        elif 'down' in command:
            speak('volume decreasing'+'sir')
            pg.press('volumedown')
        elif 'mute' in command:
            speak('muting'+'sir')
            pg.press('volumemute')
        elif 'rest' in command:
            speak('see you soon, sir')
            break
        elif 'visual' in command:
            speak('opening' +'' +'sir')
            os.startfile('"C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
        elif 'delete' in command:
            delete()
        elif 'zen' in command:
            speak('calling zen, sir')
            os.startfile("D:\\talha coding\\web design projects\\python\\VR mouse.py")
        elif 'position' in command:
            os.startfile('D:\\talha coding\\web design projects\\python\\position.py')
            speak('Tracking cursor position,sir')
        elif 'battery' in command:
            battery = psutil.sensors_battery().percent
            speak("Battery level is"+str(battery)+"sir" )
        elif 'send' in command:
            name = command.replace("send" , "")
            speak('what is the message')
            message = take_command()
            print(name)
            print(message)
            whatsappMsg(name, message)
        elif 'tell' in command:
            name = command.replace("tell" , "")
            speak('what is the message')
            message = take_command()
            print(name)
            print(message)
            messenger(name, message)
        elif 'clear' in command:
            pg.hotkey('win', 'd')
            speak('cleared,sir')
        elif 'take notes' in command:
            pg.press('win')
            pg.write('stickey') 
            pg.press('enter')
        elif 'logout' in command:
            log_out()
        elif 'night' in command:
            nightmode()
        elif 'bluetooth' in command:
            bluetooth()
        elif 'birthday' in command:
            os.startfile('D:\\talha coding\\web design projects\\python\\Birthday.py')
            speak('function opened')
        elif 'downloader' in command:
            os.startfile('D:\\talha coding\\web design projects\\python\\yt downloader.py')
            speak('function opened')
        else:
            speak('i didnt get it,sir')
            speak('if you dont mind then could you please say it again, sir')
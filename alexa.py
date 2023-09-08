
#!/usr/bin/python3
import speech_recognition as sr
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
from time import ctime
import webbrowser
import subprocess
import pygame
import os
import time
import pyautogui as pya
import psutil




def play_music():
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load the music file
    pygame.mixer.music.load("fav.mp3")
    
    # Play the music
    pygame.mixer.music.set_volume(3)
    pygame.mixer.music.play()
    
    time.sleep(20)
    pygame.mixer.music.stop()


myfav_links=["https://chat.openai.com/","https://mail.google.com/mail/u/0/#inbox","https://web.whatsapp.com/"]

def open_links(url):
    if "chat" in url:
        webbrowser.get("/usr/bin/google-chrome").open(url)
    else:
        webbrowser.get("/usr/bin/firefox").open(url)


def play_sound_intro():
    os.system("mpg321 intro.mp3")


def play_sound_next():
    os.system("mpg321 -g 300 next.mp3")

def speak_wys(text_v):
    tts = gTTS(text=text_v, lang='en-us', slow=False, tld='com')
    tts.save("sound.mp3")
    audio = AudioSegment.from_mp3("sound.mp3")
    louder_audio = audio + 6 
    louder_audio.export("louder_sound.mp3", format="mp3")
    play(louder_audio)
    # os.system("mpg321 sound.mp3")
    os.remove("sound.mp3")
    os.remove("louder_sound.mp3")

def speak_wys_arab(text_v):
    tts = gTTS(text=text_v, lang='ar', slow=False, tld='com')
    tts.save("sound.mp3")
    audio = AudioSegment.from_mp3("sound.mp3")
    louder_audio = audio + 6 
    louder_audio.export("louder_sound.mp3", format="mp3")
    play(louder_audio)
    # os.system("mpg321 sound.mp3")
    os.remove("sound.mp3")
    os.remove("louder_sound.mp3")    
    

def record(ask=False):
    if ask:
        speak_wys(ask)
    else:    
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            recognizer.adjust_for_ambient_noise(source)  
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="en")
            return text.lower()
        except sr.UnknownValueError:
            speak_wys("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        return None


def record_arb(ask=False):
    if ask:
        speak_wys_arab(ask)
    else:    
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            recognizer.adjust_for_ambient_noise(source)  
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ar")
            return text.lower()
        except sr.UnknownValueError:
            speak_wys("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        return None

inter_path=["/media/ahmed/New Volume/Embedded/Embedded Linux/C++ course","/media/ahmed/New Volume/Embedded/Embedded Linux"]
def open_dir(path):
    pya.hotkey("win")
    time.sleep(.5)
    pya.write("terminal")
    time.sleep(.5)
    pya.press("enter")
    time.sleep(1)
    pya.typewrite("nautilus "+ path)
    pya.press("enter")
    




def respond(text_v):
    if "اسمي" in text_v or "اسم" in text_v:
        play_sound_intro()
        record("your order is ganna be executed , everything under controll ,ya man")
        play_sound_next()
        speak_wys("hello ya badr, your full name is ahmed badr sayed")
        play_sound_intro()
    elif "ساكن" in text_v or "عنواني" in text_v or "انا ساكن"in text_v:
        play_sound_intro()
        record("your order is ganna be executed, everything under controll,  ya man")
        play_sound_next()
        speak_wys("okay ya badr, you live in Shobra Elkhyma")
        play_sound_intro()
    elif "الساعه" in text_v or "الوقت" in text_v:
        play_sound_intro()
        record("your order is ganna be executed , everything under controll,  ya man")
        play_sound_next()
        speak_wys("the full time is  "+ ctime() +"that is includeded day , month, year full expersion to be up to date")
        play_sound_intro()
    elif "الاغنيه" in text_v or "بحبها"  in text_v or "اغنيه" in text_v:
        play_sound_intro()
        record("your order is ganna be executed , everything under controll,  ya man")
        play_sound_next()
        play_music()
        play_sound_intro() 
        speak_wys("i have played your favourite music, just for 20 sec")
        play_sound_next()
    elif 'خلاص' in text_v or "شكرا" in text_v or "مع السلامه" in text_v:
        play_sound_intro()
        record("thanks alot my friend to use me as your assistant, i have wished i were your best companion, goodbye")
        play_sound_next()
        exit()    
    elif 'البطارية' in text_v  or "الشحن" in text_v or "نسبة" in text_v:
        play_sound_intro()
        speak_wys("the charge percentage  will be calculated, just seconds")
        play_sound_next() 
        speak_wys(f"your battery percentage is ,{int(psutil.sensors_battery().percent)} %")
        play_sound_intro()    
    elif  "جيميل" in text_v:
       play_sound_intro()
       speak_wys("your order is ganna be executed , everything under controll")
       play_sound_next() 
       open_links(myfav_links[1])
       play_sound_intro()
    elif "الكورس" in text_v or "الامبيديد" in text_v or "كورس" in text_v or "اللينكس" in text_v or "القرص" in text_v:
       play_sound_intro()
       speak_wys("your order is ganna be executed , just seconds")
       play_sound_next() 
       open_dir("  " + str(inter_path[1]))
       play_sound_intro()
    elif "الشات" in text_v or "بي تي" in text_v :
       play_sound_intro()
       speak_wys("your order is ganna be executed , just seconds")
       play_sound_next() 
       open_links(myfav_links[0])
       play_sound_intro()
    elif "واتساب" in text_v or "الواتس" or "تس" in text_v :
       play_sound_intro()
       speak_wys("your order is ganna be executed , just seconds")
       play_sound_next() 
       open_links(myfav_links[2])
       play_sound_intro()   
    


flag = None
while flag is None:
    source = record()
    if "hay" in source or "hello" in source or "hi" in source or "alexa" in source:
        play_sound_intro()
        speak_wys("hi myfriend this is me Alexa you can call me my assistant as you like let do it , can I help you")
        play_sound_intro()
        flag = 1

while True:
    voice_data = record_arb()
    if voice_data:
        respond(voice_data)





from time import strftime

import pyttsx3

import speech_recognition as sr

import pyaudio

import os

import datetime

import webbrowser

import openai

engine = pyttsx3.init('nsss')

voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

# text to speech

def speak(audio):
engine.say(audio)

 print(audio)

 engine.runAndWait()

# voice to text

def takecommand():

 r = sr.Recognizer()

 with sr.Microphone() as source:

 print("listening.....")

 audio = r.listen(source)

 try:

 print("Recognizing....")

 query = r.recognize_google(audio, language='en-in')

 print(f"user said: {query}")

 except Exception as e:

 speak("Say that again please.....")

 return "Some error Occurred. Sorry from Jarvis "
return query

if _name_ == "_main_":

 speak("hello I am jarvis A.I")

 while True:

 query = takecommand()

 sites= [["youtube", "https://www.youtube.com"],["wikipedia", 

"https://www.wikipedia.com"],["google", 

"https://www.google.com"],["youtube", "https://www.youtube.com"]]

 for site in sites:

 if f"open {site[0]}".lower() in query.lower():

 speak(f"opening {site[0]}...")
if "the time" in query:

 strfTime = datetime.datetime.now().strftime("%H:%M:%S")

 speak(f"The time is {strfTime}")

 if "open photos".lower() in query.lower():

 os.system("open /System/Applications/Photos.app")

 if "open maps".lower() in query.lower():

 os.system("open /System/Applications/Maps.app")

 if "open facetime".lower() in query.lower():

 os.system("open /System/Applications/FaceTime.app")

 webbrowser.open(site[1])

 if "open music" in query:

 musicPath = "/Users/hindu/Downloads/theme-timeless-vlog-no-

copyright-music-195165.mp3"

 os.system(f"open {musicPath}")

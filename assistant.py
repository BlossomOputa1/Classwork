import pyttsx3 as pt
import pyaudio as pa
import speech_recognition as sr
import flet as ft
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.9)


def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hey there, I am your voice assistant, how are you doing")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Say something!")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am also having a great day")
speak("how can i be of help to you")
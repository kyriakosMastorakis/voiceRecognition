import pyttsx3
import time

from pyttsx3 import engine


def speak(text,speed,voiceIndex):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate',speed)

    engine.setProperty('volume', 0.9)

    fones =  engine.getProperty('voices')
    if 0 <= voiceIndex <= len(fones):
        engine.setProperty('voice', fones[voiceIndex].id)

    engine.say(text)
    engine.runAndWait()

engineTemp = pyttsx3.init()
fones = engineTemp.getProperty('voices')

print("available voices:")
for i,v in enumerate(fones):
    print(i, "-",v.name)

speed = int(input("Give me speed(50 - 200): "))

voiceChoice = int(input("choose number of voice: "))

usertext = input("enter your text:")
speak(usertext,speed,voiceChoice)



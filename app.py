import os
from gtts import gTTS
from playsound import playsound

text = "I am Jeman Park"

tts = gTTS(text=text, lang='en')

tts.save("hi.mp3")
playsound("hi.mp3")
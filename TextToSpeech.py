from playsound import playsound
from gtts import gTTS
import os
import time

try:
    while True:

        tex = input("What is it? ")
        print("")
        tts = gTTS(text=tex, lang='en')
        tts.save("sound.mp3")
        playsound('sound.mp3')
        os.remove("sound.mp3")
        time.sleep(.5)

finally:

    print("")
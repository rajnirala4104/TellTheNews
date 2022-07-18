from googletrans import Translator
from gtts import gTTS
import playsound
import os

transEg = Translator()
def speak(str, language):
    while 1:
        trans = transEg.translate(str, dest=language)
        converted = gTTS(trans.text, lang = language)
        converted.save('sound.mp3')
        # asdkstp = input("Enter stop to Stop the news: ")
        playsound.playsound('sound.mp3', True)
        os.remove("sound.mp3")

if __name__=="__main__":
    speak("Hello friends, my name is raj nirala .", "fr")
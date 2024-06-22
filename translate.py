from googletrans import Translator
from gtts import gTTS
import playsound
import os

transEg = Translator()
def speak(str, language):
    """
    This function takes a string and a language as input and translates the string to the specified language.
    It then converts the translated text to speech and saves it as an mp3 file.
    The function plays the audio file and removes it once it has finished playing.
    
    Args:
        str (str): The string to be translated and spoken.
        language (str): The language to which the string should be translated.
    """
    # Enter an infinite loop to continuously translate and speak the input string
    while True:
        # Translate the input string to the specified language
        trans = transEg.translate(str, dest=language)
        # Convert the translated text to speech and save it as an mp3 file
        converted = gTTS(trans.text, lang = language)
        converted.save('sound.mp3')
        # Print a loading message
        print("loading..")
        # Play the audio file
        playsound.playsound('sound.mp3', True)
        # Remove the audio file once it has finished playing
        os.remove("sound.mp3")
        os.remove('news.txt')

if __name__=="__main__":
    speak("Hello friends, my name is raj nirala .", "fr")
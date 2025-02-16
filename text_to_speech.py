from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(text):
    try:
        tts = gTTS(text, lang='en')
        audio_file = "Summary.mp3"
        tts.save(audio_file)

        print("Playing the audio...")
        playsound(audio_file)

        #os.remove(audio_file)
        print("FINISHED")
    except Exception as e:
        print(f"Error: {e}")

from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer
from gtts import gTTS
import time
import os

class TTS:
    def __init__(self) -> None:
        mixer.init()
        mixer.quit()
        mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")
    
    def speak(self, text: str) -> None:
        gTTS(text=text, lang='en-uk').save("text.mp3")
        
        mixer.music.load("text.mp3")
        mixer.music.play()
        
        while mixer.music.get_busy():
            time.sleep(0.3)
            
        mixer.music.unload()

    def removeAudioFile(self) -> None:
        if os.path.exists("text.mp3"):
            os.remove("text.mp3")
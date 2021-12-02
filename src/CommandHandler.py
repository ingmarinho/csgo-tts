import keyboard
import threading
import time
from queue import Queue

from LogFileParser import LogFileParser
from TTS import TTS
import Config


def CommandHandler(logFileParser: LogFileParser, tts: TTS, queue: Queue) -> None:
    thread = threading.current_thread()
    
    while getattr(thread, "running", True):
        while getattr(thread, "paused", True):
            time.sleep(1)
            
        if not queue.empty():
            speakText(tts, queue.get())
            
        line = logFileParser.readLastLine()
        if line is None:
            time.sleep(0.3)
            continue
        
        queue.put(line)


def speakText(tts: TTS, text: str) -> None:
    keyboard.press(Config.VOICE_KEY)
    
    print(f"[ Playing: '{text}' ]")
    
    tts.speak(text)
    tts.removeAudioFile()
    
    keyboard.release(Config.VOICE_KEY)
import keyboard
import threading
import time

from LogFileParser import LogFileParser
from TTS import TTS
import Config


def CommandHandler(logFileParser: LogFileParser, tts: TTS) -> None:
    thread = threading.current_thread()
    
    while getattr(thread, "running", True):
        while getattr(thread, "paused", True):
            time.sleep(1)
            
        line = logFileParser.readLastLine()
        if line is None:
            time.sleep(0.4)
            continue
    
        tts.speak(line)
        keyboard.release(Config["CSGO"]["voiceKey"])
        
        tts.removeAudioFile()


# def main():
#     commandHandler = threading.Thread(target=CommandHandler)
#     commandHandler.start()
#     # time.sleep(5)
#     # t.running = False
    

# if __name__ == "__main__":
#     main()
    
    
# class CommandHandler:
#     def __init__(self) -> None:
#         pass
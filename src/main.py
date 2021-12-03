import Requirements

from queue import Queue
from threading import Thread
import keyboard

from CommandHandler import CommandHandler, pause, addCustomToQueue
from LogFileParser import LogFileParser, ChatPrefix
from TTS import TTS
import Config


logFileParser = LogFileParser()
tts = TTS()
queue = Queue(maxsize=5)


def main() -> None:
    # Emptying logfile at program start
    logFileParser.emptyLogFile()
    
    # loading prefixes
    logFileParser.setPrefix([prefix for prefix in ChatPrefix if prefix.name in Config.PREFIXES])
    
    commandHandlerThread = Thread(target=CommandHandler, args=(logFileParser, tts, queue))
    commandHandlerThread.start()
    commandHandlerThread.paused = False

    # loading default binds
    keyboard.add_hotkey(Config.PAUSE_KEY, pause, args=(commandHandlerThread,))
    if Config.CLEAN_LOGFILE_KEY != "": keyboard.add_hotkey(Config.CLEAN_LOGFILE_KEY, logFileParser.cleanLogFile)
    if Config.EMPTY_LOGFILE_KEY != "": keyboard.add_hotkey(Config.EMPTY_LOGFILE_KEY, logFileParser.emptyLogFile)

    # loading custom binds
    if Config.CUSTOM_BINDS:
        for key in Config.CUSTOM_BINDS:
            keyboard.add_hotkey(key[0], addCustomToQueue, args=(commandHandlerThread, queue, key[1]))

    keyboard.wait(Config.STOP_KEY)
    commandHandlerThread.paused = False
    commandHandlerThread.running = False

    print("Finished!")


if __name__ == "__main__":
    main()
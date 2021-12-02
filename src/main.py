from queue import Queue
from threading import Thread
import keyboard

from CommandHandler import CommandHandler
from LogFileParser import LogFileParser, ChatPrefix
from TTS import TTS
import Config

logFileParser = LogFileParser()
tts = TTS()
queue = Queue(maxsize=5)


# def getVirtualDevice() -> str:
#     virtualInput: str = "CABLE Input (VB-Audio Virtual Cable)"

#     if not virtualInput in [get_audio_device_name(i, 0).decode() for i in range(get_num_audio_devices(0))]:
#         raise Exception("Please make sure you have VBCable installed!")

#     return virtualInput


def pause(commandHandlerThread: Thread) -> None:
    if commandHandlerThread.paused:
        commandHandlerThread.paused = False
        print("[ CommandHandler has been unpaused ]")
    else:
        commandHandlerThread.paused = True
        print("[ CommandHandler has been paused ]")


def addCustomToQueue(commandHandlerThread: Thread, text: str) -> None:
    if not commandHandlerThread.paused: queue.put(text)


def main() -> None:
    # Emptying logfile at program start
    logFileParser.emptyLogFile()
    
    commandHandlerThread = Thread(target=CommandHandler, args=(logFileParser, tts, queue))
    commandHandlerThread.start()
    commandHandlerThread.paused = False

    # loading default binds
    keyboard.add_hotkey(Config.PAUSE_KEY, pause, args=(commandHandlerThread,))
    keyboard.add_hotkey(Config.CLEAN_LOGFILE_KEY, logFileParser.cleanLogFile)
    keyboard.add_hotkey(Config.EMPTY_LOGFILE_KEY, logFileParser.emptyLogFile)

    # loading custom binds
    for key in Config.CUSTOM_BINDS:
        keyboard.add_hotkey(key[0], addCustomToQueue, args=(commandHandlerThread, key[1]))

    keyboard.wait(Config.STOP_KEY)
    commandHandlerThread.paused = False
    commandHandlerThread.running = False

    print("Finished!")


if __name__ == "__main__":
    main()
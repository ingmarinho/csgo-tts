# from queue import Queue
from threading import Thread
import keyboard

from CommandHandler import CommandHandler
from LogFileParser import LogFileParser, ChatPrefix
from TTS import TTS
import Config

logFileParser = LogFileParser()
tts = TTS()
# queue = Queue(maxsize = 0)


# def getVirtualDevice() -> str:
#     virtualInput: str = "CABLE Input (VB-Audio Virtual Cable)"

#     if not virtualInput in [get_audio_device_name(i, 0).decode() for i in range(get_num_audio_devices(0))]:
#         raise Exception("Please make sure you have VBCable installed!")

#     return virtualInput


def pause(commandHandlerThread: Thread) -> None:
    if commandHandlerThread.paused:
        commandHandlerThread.paused = False
        print("CommandHandler has been unpaused")
    else:
        commandHandlerThread.paused = True
        print("CommandHandler has been paused")
        
    # commandHandlerThread.paused = False if commandHandlerThread.paused else True
    # print("CommandHandler has been paused")

# def stop(commandHandlerThread: Thread) -> None:
#     commandHandlerThread.running = False
#     print("CommandHandler has been stopped!")
    
def main() -> None:
    
    commandHandlerThread = Thread(target=CommandHandler, args=(logFileParser, tts))
    commandHandlerThread.start()
    commandHandlerThread.paused = False
    
    keyboard.add_hotkey(Config.PAUSE_KEY, pause, args=(commandHandlerThread,))
    # keyboard.add_hotkey(Config.STOP_KEY, stop, args=(commandHandlerThread,))
    keyboard.add_hotkey(Config.CLEAN_LOGFILE_KEY, logFileParser.cleanLogFile)
    keyboard.add_hotkey(Config.EMPTY_LOGFILE_KEY, logFileParser.emptyLogFile)
    
    keyboard.wait(Config.STOP_KEY)
    commandHandlerThread.paused = False
    commandHandlerThread.running = False
    
    print("Done!")
    # time.sleep(5)
    # t.running = False
    # while True:
    #     x = logFileParser.readLastLine()
    #     print(x)
    #     time.sleep(0.5)
    
    
    # mixer.init()
    # virtualInputDevice: str = getVirtualDevice()
    # mixer.quit()
    # mixer.init(devicename=virtualInputDevice)

    # while True:
        
        
        # time.sleep(0.5)

        # cleanLogFile()

        # if textQueue == []:
        #     addTextToQueue()
        # else:
        #     removeTextFromFile(textQueue)
        #     validText: str = textQueue[0][textQueue[0].find(':') + 1:].strip()
        #     gTTS(text=validText, lang='en-uk').save("text.mp3")
        #     mixer.music.load("text.mp3")
        #     keyboard.press(VOICE_KEY)
        #     mixer.music.play()
        #     textQueue.pop(0)
        #     while mixer.music.get_busy():
        #         time.sleep(1)
        #     mixer.music.unload()
        #     keyboard.release(VOICE_KEY)

        #     if os.path.exists("text.mp3"):
        #         os.remove("text.mp3")


if __name__ == "__main__":
    main()

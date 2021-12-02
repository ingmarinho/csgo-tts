from configparser import ConfigParser

configParser = ConfigParser()
configParser.read("./config.ini")

USERNAME = configParser["STEAM"]["username"]
LOGFILE_DIR = configParser["STEAM"]["csgoPath"] + "\console.log"

VOICE_KEY = configParser["CSGO"]["voiceKey"]

PAUSE_KEY = configParser["BINDS"]["pauseToggle"]
STOP_KEY = configParser["BINDS"]["stopRunning"]
CLEAN_LOGFILE_KEY = configParser["BINDS"]["cleanLogFile"]
EMPTY_LOGFILE_KEY = configParser["BINDS"]["emptyLogFile"]
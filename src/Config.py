from configparser import ConfigParser
from os.path import exists

configParser = ConfigParser()
configParser.read("./config.ini")

assert configParser["STEAM"]["username"] != "", "Please fill in your Steam username in the config.ini file"
USERNAME = configParser["STEAM"]["username"]

assert configParser["STEAM"]["csgoPath"] != "", "Please fill in your CSGO path in the config.ini file"
assert exists(configParser["STEAM"]["csgoPath"] + "\console.log"), "Please make sure -condebug has been added to your CSGO launch options, if this is the case make sure CSGO is running before starting this program"
LOGFILE_DIR = configParser["STEAM"]["csgoPath"] + "\console.log"


assert configParser["CSGO"]["voiceKey"] != "", "Please fill in your CSGO voice key in the config.ini file"
VOICE_KEY = configParser["CSGO"]["voiceKey"]

assert configParser["CSGO"]["prefixes"] != "", "Please fill in youre preferred prefixes in the config.ini file"
PREFIXES = configParser["CSGO"]["prefixes"].strip().split(" + ")


assert configParser["BINDS"]["pauseToggle"] != "", "Please fill in your preferred pause toggle key in the config.ini file"
PAUSE_KEY = configParser["BINDS"]["pauseToggle"]

assert configParser["BINDS"]["stopRunning"] != "", "Please fill in your preferred stop key in the config.ini file"
STOP_KEY = configParser["BINDS"]["stopRunning"]

CLEAN_LOGFILE_KEY = configParser["BINDS"]["cleanLogFile"]
EMPTY_LOGFILE_KEY = configParser["BINDS"]["emptyLogFile"]


# loading custom binds
configParser.read("./custom.ini")

CUSTOM_BINDS = [(key, configParser["CUSTOM"][key]) for key in configParser["CUSTOM"]] if len(configParser["CUSTOM"]) > 0 else None

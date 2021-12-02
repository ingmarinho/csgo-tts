from file_read_backwards import FileReadBackwards
from enum import Enum
import Config

class ChatPrefix(Enum):
    TEAM = (f"(Counter-Terrorist) {Config.USERNAME}", f"(Terrorist) {Config.USERNAME}")
    TEAM_DEAD = (f"*DEAD*(Counter-Terrorist) {Config.USERNAME}", f"*DEAD*(Terrorist) {Config.USERNAME}")
    ALL = (Config.USERNAME,)
    ALL_DEAD = (f"*DEAD* {Config.USERNAME}")
    
    def prefixValue(self) -> tuple:
        return self.value
        

class LogFileParser:
    def __init__(self) -> None:
        self.logFileDir = Config.LOGFILE_DIR
        self.selectedPrefixes = ChatPrefix.ALL.prefixValue()
        self.previousLine = str()
    
    def readLastLine(self) -> str | None:
        with FileReadBackwards(self.logFileDir, encoding="utf-8") as logFile:
            line = logFile.readline()
            
            if line == self.previousLine: return None
            self.previousLine = line
            
            return line[line.find(':') + 1:].strip() if line.startswith(self.selectedPrefixes) else None
    
    def setPrefix(self, *prefixes: ChatPrefix) -> None:  
        self.selectedPrefixes = sum(tuple([prefix.prefixValue() for prefix in prefixes]), ())
    
    def cleanLogFile(self) -> None:
        with open(self.logFileDir, "r+", encoding="utf-8") as logFile:
            lines: list = logFile.readlines()

            logFile.seek(0)
            logFile.truncate()

            for line in lines:
                if line.startswith(self.selectedPrefixes):
                    logFile.write(line)
    
    def emptyLogFile(self) -> None:
        with open(self.logFileDir, 'w'): pass
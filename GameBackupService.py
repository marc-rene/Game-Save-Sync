import os, time, sys, subprocess, shutil, json
import logging as log
from pathlib import Path
from enum import Enum

class Game:
    Name = "Unknown Game"
    LocalSavePath = Path()
    OffsiteSavePath = Path()

    def __init__(self, gameName: str, localSavePath: Path, offSiteSavePath: Path):
        Name = gameName
        LocalSavePath = localSavePath
        offSiteSavePath = offSiteSavePath


    def __str__(self):
        return f"Name: {self.Name}, Local: {self.LocalSavePath.as_posix}, Offsite: {self.OffsiteSavePath.as_posix}"
    


class ErrorType(Enum):
    all_good = 1
    appdata_permission_error = 2
    no_config_detected = 3


class GameBackupService:
    ErrorStatus = ErrorType.all_good
    AppDataLocal = Path()
    ConfigPath = Path()
    Config: None

    def SetDefaultEnvSettings(self):
        log.info(f"Appdata found at: {Path(os.getenv('LOCALAPPDATA'))}")
        self.AppDataLocal = Path(os.getenv('LOCALAPPDATA')) / "Game Save Sync"
        self.ConfigPath = self.AppDataLocal / "config.json"

    def TestEnviorment(self):
        log.debug("Checking out enviorment")
        try:

            log.debug(f"Making our config file @ {self.ConfigPath.absolute()}")
            self.AppDataLocal.mkdir(parents=True, exist_ok=True)


            if self.ConfigPath.exists() == False:
                log.warning(f"Config file doesn't exist! Making our config folder in {self.ConfigPath.absolute()}")
                self.ErrorStatus = ErrorType.no_config_detected
            
            else:
                log.debug(f"Opening {self.ConfigPath.absolute()}")
                try:
                    with open(self.ConfigPath.absolute()) as cfgFile:
                        self.Config = json.load(cfgFile)
                        log.debug(f"Config version: {self.Config["Version"]}")   
                except Exception as cfgError:
                    log.warning(f"{self.ConfigPath.absolute()} is bollocksed because: {cfgError}")
                    self.ErrorStatus = ErrorType.no_config_detected

        except PermissionError:
            log.error(f"""  We do NOT have permission to access our config folder in {self.AppDataLocal.absolute()}
                        Please can you Game Backup Service the permission to make a config?""")
            self.ErrorStatus = ErrorType.appdata_permission_error


    def __init__(self):
        log.info(f"Game Save Sync Service Launched!")
        
        self.SetDefaultEnvSettings()
        self.TestEnviorment()
        
        match(self.ErrorStatus):
            case ErrorType.appdata_permission_error:
                exit(1)
            case _:
                self.SetDefaultEnvSettings()
        
    

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG,)

    # THANK YOU https://stackoverflow.com/a/7995762
    log.addLevelName( log.DEBUG,    "\033[1;30m%s\t\033[1;0m\t"     % log.getLevelName(log.DEBUG))
    log.addLevelName( log.INFO,     "\033[1;34m%s\t\033[1;0m\t"     % log.getLevelName(log.INFO))
    log.addLevelName( log.WARNING,  "\033[1;31m%s\t\033[1;0m\t"     % log.getLevelName(log.WARNING))
    log.addLevelName( log.ERROR,    "\033[0;33m%s\t\033[1;0m\t"     % log.getLevelName(log.ERROR))

    DummyTest = GameBackupService()


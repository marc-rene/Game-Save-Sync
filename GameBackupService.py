import os, time, sys, subprocess, shutil, json
from pathlib import Path
from enum import Enum

class Game:
    Name = "Unknown Game"
    LocalSavePath = Path()
    OffsiteSavePath = Path()

    def __init__(self, gameName: str, localSavePath: Path):
        Name = gameName
        LocalSavePath = localSavePath


class ErrorType(Enum):
    all_good = 1
    appdata_permission_error = 2
    no_config_detected = 3


class GameBackupService:
    ErrorStatus = ErrorType.all_good
    AppDataLocal = Path()
    ConfigPath = Path()
    Config: json

    def SetDefaultEnvSettings(self):
        self.AppDataLocal = Path(os.getenv('LOCALAPPDATA')) / "Game Backup Service"
        self.ConfigPath = self.AppDataLocal / "config.json"

    def TestEnviorment(self):
        try:
            self.AppDataLocal.mkdir(parents=True, exist_ok=True)

            if not self.Config.exists():
                self.ErrorStatus = ErrorType.no_config_detected

        except PermissionError:
            print(f"""  We do NOT have permission to access our config folder in {self.AppDataLocal}
                        Please can you Game Backup Service the permission to make a config?""")
            self.ErrorStatus = ErrorType.appdata_permission_error


    def __init__(self):
        self.TestEnviorment()
        
        match(self.ErrorStatus):
            case ErrorType.appdata_permission_error:
                exit(1)
            case _:
                self.SetDefaultEnvSettings()
        
    

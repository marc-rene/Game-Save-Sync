import os, time
from pathlib import Path
from enum import Enum
#from nicegui import ui

AppName = "Game Save Sync"
class UiNeeded(Enum):
    not_needed = 1
    appdata_permission_error = 2
    no_config_detected = 3
    
isUiNeeded = UiNeeded.not_needed

# Step 1: Check and see if we have any config file in APPDATA?
# Windows implementation
AppDataLocal = Path(os.getenv('LOCALAPPDATA')) / AppName

print(f"Appdata folder is {AppDataLocal}")

try:
    AppDataLocal.mkdir(parents=True, exist_ok=True)
    config_file = AppDataLocal / "config.json"
    
    if not config_file.exists():
        isUiNeeded = UiNeeded.no_config_detected
    
except PermissionError:
    print(f"""  We do NOT have permission to access our config folder in {AppDataLocal}
                Please can you allow {AppName} the permission to make a config?""")
    isUiNeeded = UiNeeded.appdata_permission_error



match(isUiNeeded):
    case UiNeeded.not_needed:
        print(f"All is good, running {AppName}")
        
    case UiNeeded.no_config_detected:
        print(f"{config_file} does not exist, running UI to make one")

    case UiNeeded.appdata_permission_error:
        print(f"We dont have permission to make {config_file} in {AppDataLocal}")

    
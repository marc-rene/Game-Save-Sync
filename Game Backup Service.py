import os, time

GSBS_autostart = True if __name__ == "__main__" else False

# - - - - - - - - - - - Folder Paths - - - - - - - - - - - - #
GSBS_Onedrive_Location = "C:\Users\cesar\OneDrive\Saved Games"

GSBS_LocalSavePaths = {
    "C:\Users\cesar\AppData\Local\Colossal Order\Cities_Skylines\Saves"
}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


while True:
    for game in GSBS_LocalSavePaths:
        local_saves = [f for f in os.listdir(game) if os.isfile(os.join(game, f))]
        
    
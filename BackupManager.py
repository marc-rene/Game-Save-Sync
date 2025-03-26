import GameBackupService, subprocess, sys, os


try:
    __import__("nicegui")

except ImportError:
    print(f"NiceGui is not insatlled. Pipping it now...")
    subprocess.run([sys.executable, "-m", "pip", "install", "nicegui"], check=True)

    # Restart the script
    os.execv(sys.executable, [sys.executable] + sys.argv)

from nicegui import ui

ui.run()
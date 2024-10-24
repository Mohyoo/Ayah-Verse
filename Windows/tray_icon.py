# This file manages the tray icon for 'Ayah' app.

import os
import sys
import pystray
from pathlib import Path
from PIL import Image        # Pillow.
import subprocess

# Just in case:
status = open('background_status.txt').read()
if status == '1':
    sys.exit()      # Already running, quit to avoid duplications.


# Necessary function.
def click(icon, message):
    """Provide the tray menu's actions."""
    global loop
    if str(message) == 'Quit':
        # Reset the background status to start later..
        status = open('background_status.txt', 'w')
        status.write('0')
        status.close()  # Close & Save.
        # Stop the main_loop process.
        main_loop = open('main_loop.txt', 'w')
        main_loop.write('0')
        main_loop.close()
        subprocess.run('taskkill /im Ayah.exe /f', creationflags=0x08000000)
        # Exit the this program.
        loop = False
        icon.stop()
    elif str(message) == 'Enable at startup':
        try:
            cmd = "powershell Start-Process -Verb runAs startup_move.bat -ArgumentList '/c dir /p' -WindowStyle Hidden -PassThru"
            subprocess.run(cmd, creationflags=0x08000000)
            startup_status.write_text('enabled')
        except:
            pass

        icon.stop()     # stop, to re-run later with a new menu.
    elif str(message) == 'Disable at startup':
        try:
            subprocess.run(f'del "{startup_path}"', shell=True, creationflags=0x08000000)
            # os.system(f'del "{bat_path}"')
            startup_status.write_text('disabled')
        except:
            pass

        icon.stop()


# Prepare paths:
startup_status = Path('startup_status.txt')
startup_path = Path('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/Ayah.vbs')
exe_path = os.path.abspath("Ayah.exe")

startup_bat = Path('startup.bat')
startup_bat.write_text(f'cd {exe_path[:-9]} & echo 0 > background_status.txt & start tray_icon.exe & start Ayah.exe')

script = ('Set WshShell = CreateObject("WScript.Shell")\n'
	     f'WshShell.Run chr(34) & "{exe_path[:-9]}\\startup.bat" & Chr(34), 0\n'
	      'Set WshShell = Nothing')
startup_vbs = Path('Ayah.vbs')
startup_vbs.write_text(script)

startup_move = Path('startup_move.bat')
startup_move.write_text(f'copy "{exe_path[:-9]}\\Ayah.vbs" "{str(startup_path)[:-8]}"')


# Stray icon static settings.
image = Image.open(f'icon.ico')
item_02 = pystray.MenuItem('Quit', click)

# Run the main loop with dynamic settings (constantly updated).
loop = True
while loop:
    if startup_status.read_text().strip() == "enabled":
        item_01 = pystray.MenuItem('Disable at startup', click)
    else:
        item_01 = pystray.MenuItem('Enable at startup', click)

    menu = pystray.Menu(item_01, item_02)
    icon = pystray.Icon('Ayah', image, 'Ayah Notifier', menu=menu)
    icon.run()

# Have to reset the icon properties, because Idk why the .stop() function
# prevent the .run() function from running again.
# Path class can auto resolve the path (/) to (\) for windows, we can give it (/) or (\\)

# This file manages the tray icon for 'Ayah' app.

# Pystray requires:
#   -gir1.2-appindicator3-0.1 on ubuntu.
#   -libappindicator-gtk3 on arch.

import os
import sys
import pystray
from pathlib import Path
from PIL import Image        # Pillow.


# Necessary function.
def click(icon, message):
    """Provide the tray menu's actions."""
    global menu, item_01
    if str(message) == 'Quit':
        # Exit & Stop the background process.
        os.system('pkill -f "Ayah Wird.py"')
        os.system('pkill -f "aplay"')
        # Reset the background status to start later..
        status = open(f'{path}/background_status.txt', 'w')
        status.write('0')
        status.close()  # Close & Save.
        # Stop the tray icon.
        icon.stop()
        exit()
    elif str(message) == 'Enable at startup':
        try:
            gnome_startup_path.write_text(startup_file)
        except:
            pass
        icon.stop()     # stop, to re-run later with a new menu.
    elif str(message) == 'Disable at startup':
        try:
            gnome_startup_path.unlink()
        except:
            pass
        icon.stop()


# Prepare paths:
path = os.path.dirname(sys.argv[0])
gnome_startup_path = Path(os.path.expanduser('~/.config/autostart/Ayah_Startup.desktop'))
startup_file = ('[Desktop Entry]\n'
                'Name=Ayah Startup\n'
                f'Icon={path}/icon.ico\n'
                'Type=Application\n'
                f'Exec=python {path}/Ayah_Startup.py\n'
                'Terminal=false\n')

# Stray icon static settings.
image = Image.open(f'{path}/icon.ico')
item_02 = pystray.MenuItem('Quit', click)
# icon.notify(title='Ayah', message='Ayah is now running in the background...')

# Run the main loop with dynamic settings (constantly updated).
while True:
    if gnome_startup_path.exists():
        item_01 = pystray.MenuItem('Disable at startup', click)
    else:
        item_01 = pystray.MenuItem('Enable at startup', click)
    menu = pystray.Menu(item_01, item_02)
    icon = pystray.Icon('Ayah', image, 'Ayah Notifier', menu=menu)
    icon.run()

# Have to reset the icon properties, because Idk why the .stop() function
# prevent the .run() function from running again.

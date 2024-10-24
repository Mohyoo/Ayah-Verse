# Import libraries.
import os
import sys
from random import choice   # choice gives only an element, choices gives an element inside [].
from time import sleep
from random import randint
from plyer import notification
import subprocess

# Necessary functions.
def check_background():
    """
    To avoid infinite background processes, we check:
    0 = inactive in the background.
    1 = active.
    """
    status = open('background_status.txt').read()
    if status == '0':
        # Start in the background.
        cmd = f'powershell $process = Start-Process -FilePath "bg_cmd.bat" -WindowStyle Hidden -PassThru'
        subprocess.run(cmd, creationflags=0x08000000)
        sleep(1)
        status = open('background_status.txt', 'w')
        status.write('1')
        status.close()    
        # A notifier.
        notification.notify(app_name="آية",
                            app_icon=f"notify.ico",
                            title="Ayah is now running in the background...",
                            message="You can stop it at any time.",
                            timeout=5,
                            )
    elif status == '1':
        sys.exit()      # Already running, quit to avoid duplications.
        

# Script settings.
path = os.getcwd()
main_loop = open('main_loop.txt', 'w')
main_loop.write('1')
main_loop.close()

# Set up the background process.
check_background()

# Open and get every ayah separated.
text = open(f'Quran-simple.txt', encoding="utf8")
QURAN = text.read().strip().splitlines()[:-28]
text.close()

for line in QURAN[:]:
    line = line.strip()
    if not line:
        QURAN.remove(line)
    elif line == 'بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ':
        QURAN.remove(line)
    elif 'بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ' in line:
        index = QURAN.index(line)
        new_line = line.replace('بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ', '').strip()
        QURAN[index] = new_line

try:
    main_loop = open('main_loop.txt').read().strip()
    while main_loop == '1':
        main_loop = open('main_loop.txt').read().strip()
        # Randomly choose & send an ayah.
        ayah = choice(QURAN).strip()

        # In case it too long.
        if len(ayah) > 256:
            ayah = ayah[:253]
            while not ayah.endswith(' '):
                ayah = ayah[:-1]
            
            ayah += '...'

        sleep(randint(2700, 4500))  	# 3600s = 1h.

        # Send the notification.
        notification.notify(app_name="آية",
                            app_icon=f"notify.ico",
                            title="...لا تنس وردك",
                            message=ayah,
                            timeout=15,
                            )

except:
    status = open(f'background_status.txt', 'w')
    status.write('0')
    status.close()
    sys.exit()


sys.exit()

# include all quran + tafsir. + voice tartil.
# athkar + hadith.

# change thge desktop to the user.
# force kill problem (kill bfr bg reset).

# Import libraries.
import os
import sys
from setproctitle import setproctitle, setthreadtitle
from random import choice   # choice gives only an element, choices gives an element inside [].
from time import sleep
from notifypy import Notify


# Necessary functions.
def check_background():
    """To avoid infinite background processes, we check."""
    # 0 = inactive in the background.
    # 1 = active temporarily (while switching to (2), to avoid duplication & notification at startup).
    # 2 = active permanently.
    status = open(f'{path}/background_status.txt').read()
    if status == '0':
        # Start in the background.
        status = open(f'{path}/background_status.txt', 'w')
        status.write('1')
        status.close()
        os.system(f'nohup python {path}/Ayah.py > {path}/background.log &')
        os.system(f'nohup python {path}/tray_icon.py > {path}/tray_icon.log &')
        # A notifier.
        notification = Notify()
        notification.application_name = 'آية'
        notification.title = 'Ayah is now running in the background...'
        notification.message = 'You can stop it at any time.'
        notification.icon = f'{path}/icon.ico'
        notification.audio = f'{path}/notification_sound_01.wav'
        notification.send()
        exit()
    elif status == '1':
        status = open(f'{path}/background_status.txt', 'w')
        status.write('2')
        status.close()
    elif status == '2':
        quit()      # Already running, quit to avoid duplications.


# Set up the background process.
path = os.path.dirname(sys.argv[0])
PROCESS_NAME = 'Ayah Wird.py'
setproctitle(PROCESS_NAME)     # Not the same name as the script.
setthreadtitle(PROCESS_NAME)
check_background()

# Open and get every ayah separated.
text = open(f'{path}/Quran.txt')
QURAN = text.read().strip().splitlines()
text.close()

# Prepare the notification.
notification = Notify()
notification.application_name = 'آية'
notification.title = 'لا تنس وردك...'
notification.icon = f'{path}/icon.ico'
notification.audio = f'{path}/notification_sound_01.wav'

try:
    while True:
        # Randomly choose an ayah.
        ayah = choice(QURAN).strip()
        sleep(3600)  # 3600s = 1h.

        # Send the notification.
        notification.message = ayah
        notification.send()
except:
    status = open(f'{path}/background_status.txt', 'w')
    status.write('0')
    status.close()
    exit()

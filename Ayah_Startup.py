# This file is automatically started after login on Gnome after manual configuration.

import os
import sys

# Autostart for Gnome.
# If you want to use the GNOME way, you'll have to create a .desktop file (launcher).
# You can put it in ~/.config/autostart then you'll see that it's already included in your startup programs.

# Something like this:
#   [Desktop Entry]
#   Name=GpuPowerMizer
#   Icon=whatever
#   Type=Application
#   Exec=/usr/bin/nvidia-settings -a "[gpu:0]/GpuPowerMizerMode=1"
#   Terminal=false

# Autostart for windows.
# A batch file in startup folder.

# Set the status to (1) to avoid notifications.
path = os.path.dirname(sys.argv[0])
status = open(f'{path}/background_status.txt', 'w')
status.write('1')
status.close()
os.system(f'nohup python {path}/Ayah.py > {path}/background.log &')
os.system(f'nohup python {path}/tray_icon.py > {path}/tray_icon.log &')

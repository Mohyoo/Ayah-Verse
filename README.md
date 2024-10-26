# Description:
1) An app that displays an Ayah (verse) of the Quran (as a notification) from time to time.
2) Super light, no UI, just a tray icon.
3) For linux, it should only work on Gnome.

# Installation for Windows:
1) Just download the portable zip file from the release page.

# Installation for Linux:
Requirements (Python libraries): <br>
1) setproctitle
2) notifypy
3) pystray (also requires 'libappindicator-gtk3').
4) PIL (pillow)
<br>


Final steps: <br>
1) Download the "Linux" folder & Put it wherever you want.
2) Edit the text of (menulibre-آية.desktop) according to where you have put the 'Ayah' folder..
3) Copy (menulibre-آية.desktop) to (/home/username/.local/share/applications/).
4) Log out if necessary. <br>

5) You can install the requirements by installing python first, then in a terminal, type 'pip install requirement_name'.

# Known Issues:
1) Windows OS may detect it as a Trojan, maybe because it has access to the command line; and I will try to fix this when possible.

import os
from pathlib import Path

startup_path = Path('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/Ayah.bat')
exe_path = os.path.abspath("Ayah.exe")
startup_cmd = Path(f'startup_cmd.bat')
startup_cmd.write_text(f'echo cd {exe_path[:-8]} ^& start Ayah.exe > "{startup_path}"')
startup_status = Path('startup_status.txt')
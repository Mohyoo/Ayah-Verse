from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['_ctypes', 'ctypes', 'plyer'],
                 'excludes': []}

base = 'gui'

executables = [
    Executable('Ayah.py', base=base, icon="icon.ico"),
    Executable('tray_icon.py', base=base),
]

setup(name='Ayah',
      version = '1.0',
      description = 'Daily Quran Notifier',
      options = {'build_exe': build_options},
      executables = executables)

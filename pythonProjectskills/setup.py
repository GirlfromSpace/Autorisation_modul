from cx_Freeze import setup, Executable

excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml',
            'unicodedata', 'bz2', 'select']

zip_include_packages = ['collections', 'encodings', 'importlib', 'wx']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}
setup(
    name = "SpacePass",
    version = "0.1",
    description = "Spacepass",
    executables = [Executable("main.py", target_name='SpacePass.exe', base='Win32GUI')],
    options=options
)
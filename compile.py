import os
import subprocess

def ensure_pyinstaller_installed():
    try:
        import pyinstaller
    except ImportError:
        subprocess.check_call(['pip', 'install', 'pyinstaller'])


def compile(file_path):
    os_name = os.name
    if os_name == 'nt': # Windows
        os.system(f'pyinstaller --onefile {file_path}')
    else:
        os.system(f'pyinstaller --onefile -n {file_path}')

ensure_pyinstaller_installed()
compile(input('Enter the path to file to compile: '))
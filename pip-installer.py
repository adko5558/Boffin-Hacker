import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(script_dir, "requirements.txt")

if not os.path.exists(requirements_path):
    create = input("\033[1;33mrequirements.txt not found! Create? y/n ")
    if create.lower() == "y":
        with open(requirements_path, "w") as f:
            f.write("asyncio\nbleak\n")
        print(f"\033[1;33mCreated: {requirements_path} with asyncio and bleak.")

if os.path.exists(requirements_path):
    print("\033[1;33mInstalling packages from requirements.txt...\033[0m")
    subprocess.run([os.sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
    print("\033[1;33mInstallation completed.")
    print("This code is by Adko5558 for Boffin Hacker! Do not edit! Thank you for using our apps :D\033[0m")

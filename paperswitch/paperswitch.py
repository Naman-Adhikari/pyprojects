import os
import subprocess
import time
import random
from pathlib import Path

wall_env = os.environ.get("wallpaper")
if not wall_env:
    ip = input("Enter full path for the image directory: ").strip()
    wall_env = ip  

    user_shell = Path(os.environ.get("SHELL", "")).name  

    if user_shell == "bash":
        rcfile = Path.home() / ".bashrc"
        with open(rcfile, "a") as f:
            f.write(f'\nexport wallpaper="{wall_env}"\n')

    elif user_shell == "zsh":
        rcfile = Path.home() / ".zshrc"
        with open(rcfile, "a") as f:
            f.write(f'\nexport wallpaper="{wall_env}"\n')

    elif user_shell == "fish":
        rcfile = Path.home() / ".config/fish/config.fish"
        rcfile.parent.mkdir(parents=True, exist_ok=True)  
        with open(rcfile, "a") as f:
            f.write(f'\nset -Ux wallpaper "{wall_env}"\n')

    else:
        print(f"Unknown shell: {user_shell}, not updating rcfile")

p = Path(wall_env)
image = (file for pattern in ["*png", "*jpg", "*jpeg"] for file in p.rglob(pattern))
lstimage = list(image)
n = len(lstimage)

img = random.choice(lstimage)

if subprocess.call(["pgrep", "-x", "swww"], stdout=subprocess.DEVNULL) != 0:
    subprocess.Popen(["swww", "init"])
    time.sleep(1)

subprocess.run(["swww", "img", str(img)])


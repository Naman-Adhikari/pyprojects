import subprocess
from pathlib import Path

sort_source = input("Write the full path of folder to sort : ~/")
s_source = Path.home() / sort_source

img_src = (file for pattern in ["*png", "*jpg", "*jpeg"] for file in s_source.rglob(pattern))
ip = input("\nWrite the destination for image: ~/")
img_dst = Path.home() / ip 


img_srclst = list(img_src)
for i in range(len(img_srclst)):
    img = subprocess.run(["mv", img_srclst[i], img_dst], capture_output=True, text=True)
    if img.returncode == 1:
        print("Error: ", result.stderr)

        

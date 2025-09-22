import subprocess

a = int(input("from: "))
b = int(input("to: "))
for i in range(a, b):
    subprocess.run(["home-manager", "remove-generations", str(i)])


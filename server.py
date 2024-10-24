import subprocess
import time

command = comando = "pwd"

while True:
    out = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(out.stdout)
    time.sleep(2)
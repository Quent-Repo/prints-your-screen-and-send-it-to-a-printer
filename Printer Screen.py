from mss import mss
import subprocess

def main():
    while(True):
        with mss() as sct:
            filename = sct.shot(output="desktop.png")
            subprocess.run(["lp", "-n", "1", "desktop.png"])
main()

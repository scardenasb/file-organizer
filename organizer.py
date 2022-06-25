import os
import shutil
import sys
import time


# TODO: Look a way to sync the bar with the scrip time proccess
toolbar_width = 60

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("#")
    sys.stdout.flush()

sys.stdout.write("]\n")


downloadFolder = "/mnt/c/Users/sebad/Downloads"


def organize():
    for file in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + file)

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            os.rename(f'/mnt/c/Users/sebad/Downloads/{file}', f'/mnt/c/Users/sebad/Pictures/{file}')

        # TODO: How to call user's root windows paths from wsl/linux
        elif extension in [".iso", ".ova"]:
            shutil.move(f'/mnt/c/Users/sebad/Downloads/{file}', f'/mnt/f/Escritorio/OS/{file}')


if __name__ == "__main__":
    organize()

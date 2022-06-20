import os


downloadFolder = "/mnt/c/Users/sebad/Downloads"


def organize():
    for file in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + file)

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            os.rename(f'/mnt/c/Users/sebad/Downloads/{file}', f'/mnt/c/Users/sebad/Pictures/{file}')


if __name__ == "__main__":
    organize()


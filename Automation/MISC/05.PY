import os 
from pathlib import Path
from clearConsole import clearConsole
clearConsole()


SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
            else:
                print()
    return "MISC"

# print(pickDirectory(".pdf"))

def organizeDirectory():
    for items in os.scandir():
        if items.is_dir():
            continue
        filePath =  Path(items)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directryPath = Path(directory)
        if directryPath.is_dir() != True:
            directryPath.mkdir()
        filePath.rename(directryPath.joinpath(filePath))

print("NON")
organizeDirectory()
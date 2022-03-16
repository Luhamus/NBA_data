import os
import sys

# terminal commands, which are unfortunately os-specific

def whichOs():
    if sys.platform ==  "win32":
        return "windows"
    else:
        return "good" #  ...right?

def deleteDataDir():
    if whichOs() == "windows":
        os.system("rmdir \s Data")
    else:
        os.system("rm -r Data")


def addDataDir():
    if whichOs() == "windows":
        os.system("mkdir Data\Players")
    else:
        os.system("mkdir -p Data/Players")
    print("Created new empty Data directory")


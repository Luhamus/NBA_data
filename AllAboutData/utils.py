import os
import sys

# terminal commands, which are unfortunately os-specific
def whichOs():
    ''' Returns "windows" if used os is windows. If not, returns "good" '''

    if sys.platform == "win32":
        return "windows"
    else:
        return "good" 

def deleteDataDir():
    ''' Removes Data directory from working directroy '''

    if whichOs() == "windows":
        os.system("rmdir \\s Data")
    else:
        os.system("rm -r Data")


def addDataDir():
    ''' Adds data directory from working directroy '''

    if whichOs() == "windows":
        os.system("mkdir Data\\Players")
    else:
        os.system("mkdir -p Data/Players")
    print("Created new empty Data directory")


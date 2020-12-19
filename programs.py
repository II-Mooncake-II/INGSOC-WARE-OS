import time
from os import system, name
from datetime import datetime
import boot
import clear
import clear0
import login_ps
import login_usr
import logo
import preferences
import programs
import signUp
import start_L
import start_R
import start
import SYSTEM_FILES
import text

CEND = '\033[0m'
CRED = '\033[91m'
CBLUE = '\033[94m'
CGREEN = '\033[92m'
CYELLOW = '\033[93m'
CLAVENDER = '\033[95m'
CHID = '\033[30m'

CBRED = '\033[41m'
CBBLUE = '\033[104m'
CBGREEN = '\033[42m'
CBYELLOW = '\033[43m'
CBLAVENDER = '\033[45m'
CBWHITE = '\033[7m'

def programs():
    action = input(CRED + "ᵒ" + CYELLOW + "ᵒ" + CEND + "ᵒ PROGRAMS | " "Actions: "+ CBWHITE + "[files]" + CEND + " | " + CBWHITE + "[books]" + CEND + " | " + CBWHITE + "[text editor]" + CEND + " | " + CBBLUE + "[back]" + CEND + " | " + CBBLUE + "[log out]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " | " + CGREEN + "Type the name of the program you want to open.. " + CEND)

    if action == "back":
        clear.clear()
        start_L.start_L()
    elif action == "log out":
        clear.clear()
        login_usr.login_usr()
    elif action == "power off":
        boot.boot()
    elif action == "files":
        clear.clear()
        SYSTEM_FILES.SYSTEM_FILES()
    elif action == "text editor":
        clear.clear()
        text.textE()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear.clear()
        programs()
        pass
    pass

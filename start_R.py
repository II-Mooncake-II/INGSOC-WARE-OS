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

def start_R():
    action = input(CRED + "ᵒ" + CYELLOW + "ᵒ" + CEND + "ᵒ MENU | " "Actions: " + CBBLUE + "[sign up]" + CEND + " | " + CBBLUE + "[login]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " ")

    if action == "sign up":
        print(CRED + "User Already signed!" + CEND)
        time.sleep(2)
        clear.clear()
        start_R()
    elif action == "login":
        clear.clear()
        login_usr.login_usr()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear.clear()
        start_R()
        pass

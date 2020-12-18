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

def boot():
    clear0.clear0()
    boot = input(CGREEN + "type 'start' to boot the system.." + CEND)
    secs = 0

    if boot == "start":
        while secs != 2:
            print(CBGREEN + " booting up.. " + CEND.format(secs))
            time.sleep(7)
            secs += 2
            clear.clear()
            print(CBWHITE + "________________________________WELCOME to IngSoft 94________________________________" + CEND)
            print("Loading data..")
            time.sleep(5)

            clear.clear()
            start.start()

            print("")

    else:
        clear0.clear0()
        boot()
    pass
    pass

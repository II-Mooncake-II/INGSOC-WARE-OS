import time
from os import system, name
from datetime import datetime

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

def clear0():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        pass

#usr_signed = 0


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        logo()
pass

def logo():
    print(CRED + "██╗███╗   ██╗ ██████╗ ███████╗ ██████╗  ██████╗" + CYELLOW + "    ██╗    ██╗ █████╗ ██████╗ ███████╗" + CEND)
    print(CRED + "██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗██╔════╝" + CYELLOW + "    ██║    ██║██╔══██╗██╔══██╗██╔════╝" + CEND)
    print(CRED + "██║██╔██╗ ██║██║  ███╗███████╗██║   ██║██║ " + CYELLOW + "        ██║ █╗ ██║███████║██████╔╝█████╗" + CEND)
    print(CRED + "██║██║╚██╗██║██║   ██║╚════██║██║   ██║██║ " + CYELLOW + "        ██║███╗██║██╔══██║██╔══██╗██╔══╝" + CEND)
    print(CRED + "██║██║ ╚████║╚██████╔╝███████║╚██████╔╝╚██████╗ " + CYELLOW + "   ╚███╔███╔╝██║  ██║██║  ██║███████╗" + CEND)
    print(CRED + "╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ " + CYELLOW + "    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝" + CEND)
    print(CYELLOW + "                                                                  " + datetime.now().strftime('%m.%d %H:%M') + CEND)
    print(CRED +"_____________________________________________powered by The Big Brother._____________" + CEND)
    print(" ")
    pass

def start():
    action = input("Actions: " + CBBLUE + "[sign up]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " ")

    if action == "sign up":
        signUp()
#    elif action == "login":
#        login_check()
    elif action == "power off":
        boot()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear()
        start()
    pass
    pass

def start_R():
    action = input("Actions: " + CBBLUE + "[sign up]" + CEND + " | " + CBBLUE + "[login]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " ")

    if action == "sign up":
        print(CRED + "User Already signed!" + CEND)
        time.sleep(2)
        clear()
        start_R()
    elif action == "login":
        clear()
        login_usr()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear()
        start_R()
        pass

def preferences():
    print(CBWHITE + "PREFERENCES" + CEND + "█░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("████████████░░░░░░░░░░░░░░░░░░░░░░░░░░")

    action = input("Actions: " + CBBLUE + "[back]" + CEND + " | " + CBBLUE + "[log out]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " ")

    if action == "back":
        clear()
        start_L()
    elif action == "log out":
        clear()
        login_usr()
    elif action == "power off":
        boot()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear()
        preferences()
    pass


def start_L():
    action = input("Actions: " + CBBLUE + "[programs]" + CEND + " | " + CBBLUE + "[files]" + CEND + " | " + CBBLUE + "[preferences]" + CEND + " | " + CBBLUE + "[log out]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " ")
    if  action == "files":
        clear()
        print("Loading data..")
        time.sleep(2)
        clear()
        SYSTEM_FILES()
    elif action == "programs":
        clear()
        programs()
    elif action == "preferences":
        clear()
        preferences()
        print(CRED + "to be developed" + CEND)
    elif action == "log out":
        clear()
        login_usr()
    elif action == "power off":
        boot()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear()
        start_L()
        pass

    pass

def programs():
    print("IngSoc Apps Coming soon!")
    print("SPONSORED BY THE BIG BROTHER")
    action = input("Actions: " + CBBLUE + "[back]" + CEND + " | " + CBBLUE + "[log out]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " | " + CGREEN + "Type the name of the folder you want to open.. " + CEND)

    if action == "back":
        clear()
        start_L()
    elif action == "log out":
        clear()
        login_usr()
    elif action == "power off":
        boot()
    else:
        print(CRED + "ERR_00: No such action" + CEND)
        time.sleep(2)
        clear()
        SYSTEM_FILES()
        pass
    pass

def signUp():
    global name
    global password

    name = input("Choose a Username: " + CBWHITE)
    password = input(CEND + "Choose a Password: " + CHID)
    print(CEND + "User registered!..")
    time.sleep(2)
    clear()
    start_R()
#    usr_signed += 1
    pass

def login_usr():
    usr = input("Username: " + CBWHITE)
    if usr != name:
        print(CEND + "User not registered")
        time.sleep(2)
        clear()
        login_usr()
    else:
        login_ps()
        pass
        pass

def login_ps():
    ps = input(CEND + "Password: " + CHID)
    if ps != password:
        print(CEND + "Wrong password, try again please..")
        clear()
        login_usr()
    else:
        clear()
        print(CEND + "Loading data..")
        time.sleep(2)
        start_L()
        pass
        pass

def  SYSTEM_FILES():
        print(" ")
        print(CYELLOW + " █████       █████       █████       █████      " + CEND)
        print(CYELLOW + " █████       █████       █████       █████      " + CEND)
        print(CYELLOW + " root⮠       .cdi⮠      .gPar⮠      ingsoc⮠    " + CEND)
        print(CYELLOW + "                                                ")
        print(CYELLOW + " █████       █████       █████       █████      " + CEND)
        print(CYELLOW + " █████       █████       █████       █████      " + CEND)
        print(CYELLOW + " images⮠     other⮠     ./BBs⮠       usr⮠      " + CEND)
        print(" ")
        action = input("Actions: " + CBBLUE + "[back]" + CEND + " | " + CBBLUE + "[log out]" + CEND + " | " + CBBLUE + "[power off]" + CEND + " | " + CGREEN + "Type the name of the folder you want to open.. " + CEND)

        if action == "back":
            clear()
            start_L()
        elif action == "log out":
            clear()
            login_usr()
        elif action == "power off":
            boot()
        else:
            print(CRED + "ERR_00: No such action" + CEND)
            time.sleep(2)
            clear()
            SYSTEM_FILES()
            pass
pass

def boot():
    clear0()
    boot = input(CGREEN + "type 'start' to boot the system.." + CEND)
    secs = 0

    if boot == "start":
        while secs != 2:
            print(CBGREEN + " booting up.. " + CEND.format(secs))
            time.sleep(7)
            secs += 2
            clear()
            print(CBWHITE + "________________________________WELCOME to IngSoft 94________________________________" + CEND)
            print("Loading data..")
            time.sleep(5)

            clear()
            start()

            print("")

    else:
        clear0()
        boot()
    pass
pass


boot()



#def login_check():
#        if usr_signed == 1:
#            login_usr()
#        else:
#            print("No Users registered")
#            start()
#            pass
#pass

# ACTUAL PROGRAMMING
#else:
#    print("type 'start' to boot the system..")
#    pass

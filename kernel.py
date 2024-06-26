#--kernel.py--#
# here's a quick explanation of this:
# i haven't thinked of a way to call this,
# but this is the command line of Minux.
# you can call it DOS, but i prefer just
# to call is CMD.
from os import system, name
from datetime import datetime
# from rich import print
# ^ okay i had to remove this
# because it was fucking up the
# version, sorry

def gen_build(): 
    time = datetime.now()
    return time.strftime("%d")[1:] + time.strftime("%b")[0].upper() + time.strftime("%m")

__VER__ = "v0.03-beta"
__BUILD__ = gen_build()

class Kernel():
    def __init__(self) -> None:       
        print(f"Minux {__VER__} ({__BUILD__})")
        while True:
            command = input(">> ")
            self.execute_command(command)

    def execute_command(self, command: str):     
        if command.lower().startswith("echo"):
            text = command[len("echo "):]
            print(text)
        elif command.lower().startswith("help"):
            # YLM: okay, this one is gonna take like
            # 58954848 lines of code, be ready
            print(f"""[COMMAND LIST]
HELP{' '*6}Shows this list
ECHO{' '*6}Repeats
CLEAR/CLS{' '*6}Clears the screen
""")
        elif command.lower().startswith("clear") or command.lower().startswith("cls"):
            system('cls' if name == 'nt' else 'clear')
        else:
            print(f"unknown indetifier {command}, do HELP for the list of commands")
            return False
            
        return True
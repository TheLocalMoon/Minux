#--kernel.py--#
# here's a quick explanation of this:
# i haven't thinked of a way to call this,
# but this is the command line of Minux.
# you can call it DOS, but i prefer just
# to call is CMD.
from datetime import datetime
from rich import print

def gen_build():
    time = datetime.now()
    build = time.strftime("%d")[1:] + time.strftime("%b")[0].upper() + time.strftime("%m")
    return build

__VER__ = "v0.01"
__BUILD__ = gen_build()

class Kernel:
    def __init__(self) -> None:
        print(f"Minux {__VER__} ({__BUILD__})")
        while True:
            command = input(">> ")
            self.execute_command(command.lower())

    def execute_command(self, command: str):
        if command.startswith("echo "):
            text = command[len("echo "):]
            print(text)
        else:
            print(f"unknown indetifier {command}, do HELP for the list of commands")
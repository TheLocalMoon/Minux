#--main.py--#
# purpose: main file, what do you expect
import services, os, kernel

class Minux:
    def __init__(self) -> None:
        self.utils = services.load_service("services", "utils.py")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.kernel = kernel.Kernel() # no way, it starts the cmd!
        
if __name__ == "__main__":
    Minux()
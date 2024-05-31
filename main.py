#--main.py--#
# purpose: main file, what do you expect
import services
import kernel
import os

class Minux:
    """_summary_
    """    
    def __init__(self) -> None: 
        """_summary_
        """        
        self.utils = services.load_service("services", "utils.py")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.kernel = kernel.Kernel() # no way, it starts the command prompt!
        
if __name__ == "__main__":
    Minux()
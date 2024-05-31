#--main.py--#
import services

class Minux:
    def __init__(self) -> None:
        services.load_service("services", "test.py")

if __name__ == "__main__":
    Minux()
#--log.py--#
# the best logging system
from rich import print

class pyLOG:
    def __init__(self) -> None:
        self.disabled = False
        
    def none(self, text: str) -> None:
        print(f"{' '*8} [bold white]{text}[/bold white]")
        
    def info(self, text: str) -> None:
        print(f"[bold green][ INFO ][/bold green] [bold white]{text}[/bold white]")
        
    def warn(self, text: str) -> None:
        print(f"[bold yellow][ WARN ][/bold yellow] [bold white]{text}[/bold white]")
        
    def error(self, text: str) -> None:
        print(f"[bold red][ ERROR ][/bold red] [bold white]{text}[/bold white]")
    
    def disable(self, state: bool):
        self.disabled = state
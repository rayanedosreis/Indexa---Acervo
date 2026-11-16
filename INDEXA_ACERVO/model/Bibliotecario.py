from model.Usuario import Usuario
from rich.console import Console
from rich.panel import Panel
console = Console()

class Bibliotecario(Usuario):
    def exibirMenu(self):
        console.print(Panel("[bold bright_white]1 - Visualizar Empréstimos[/]\n"
            "[bold bright_white]2 - Visualizar Livros[/]\n"
            "[bold bright_white]3 - Sobre[/]\n"
            "[bold bright_white]4 - Sair[/]",
            title="[bold bright_cyan]MENU BIBLIOTECÁRIO[/]",border_style="bright_blue",padding=(1, 3), width=50))
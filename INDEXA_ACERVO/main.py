from model.Biblioteca import Biblioteca
from rich.console import Console
from rich.panel import Panel
console = Console()

def principal():
    exibirCarregamento()

    biblioteca = Biblioteca()
    biblioteca.carregarLivros()
    biblioteca.carregarUsuarios()
    biblioteca.carregarEmprestimos()

    while True:
        console.print(Panel("[bold bright_white]Acesse sua conta[/bold bright_white]\n"
            "[bright_white]Entre com seu login e sua senha para continuar.[/bright_white]",
            title="[bold bright_cyan]LOGIN[/bold bright_cyan]",
            border_style="bright_blue",
            padding=(1, 3),
            width=65))

        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        usuario = biblioteca.autenticarUsuario(login,senha)

        if usuario is None:
            console.print("\n[bold bright_red]✗ Login ou senha incorretos!\nTente novamente...[/]")
            continue

        console.print("[bold bright_green]✓ Login realizado com sucesso![/]")
        console.print(f"[bold bright_white]Bem-vindo(a),[/] [bold bright_cyan]{usuario.getNome()}[/]!")

        while True:
            console.print("\n")
            usuario.exibirMenu()
            opcao = console.input("\n[bold bright_cyan]Escolha uma opção:[/] ")

            if usuario.getTipo() == "Cliente":

                if opcao == "1":
                    biblioteca.listarEmprestimosCliente(usuario)
                    aguardarVolta()

                elif opcao == "2":
                    biblioteca.listarLivros()
                    aguardarVolta()


                elif opcao == "3":
                    biblioteca.listarEmprestimosCliente(usuario)
                    codigo = console.input("\n[bold bright_cyan]Digite o código do empréstimo que deseja renovar:[/]")
                    biblioteca.renovarEmprestimo(codigo, usuario)

                elif opcao == "4":
                    exibirSobre()
                    aguardarVolta()

                elif opcao == "5":
                    exibirEncerramento()
                    break

                else:
                    console.print("\n[bold bright_red]✗ Opção inválida! Tente novamente.[/]")

            elif usuario.getTipo() == "Bibliotecario":

                if opcao == "1":
                    biblioteca.listarEmprestimos()
                    aguardarVolta()

                elif opcao == "2":
                    biblioteca.listarLivros()
                    aguardarVolta()


                elif opcao == "3":
                    exibirSobre()
                    aguardarVolta()

                elif opcao == "4":
                    exibirEncerramento()
                    break

                else:
                    console.print("\n[bold bright_red]✗ Opção inválida! Tente novamente.[/]")



def exibirCarregamento():
    console.print(Panel("[bold bright_white]INDEXA[/bold bright_white]\n"
        "[bold bright_cyan]ACERVO[/bold bright_cyan] [bright_white]- Sistema de Gestão de Biblioteca[/bright_white]\n\n"
        "[bold bright_cyan]Inicializando o sistema...[/bold bright_cyan]\n"
        "[bright_white]Preparando arquivos e informações da biblioteca.[/bright_white]",
        title="[bold bright_cyan]BEM-VINDO[/bold bright_cyan]", border_style="bright_blue",padding=(1, 3),width=65))


def exibirEncerramento():
    console.print()
    console.print(Panel("[bold bright_cyan]ATÉ LOGO![/bold bright_cyan]\n\n"
        "[bold bright_white]Obrigado por utilizar o ACERVO![/bold bright_white]\n"
        "[bright_white]Até breve![/bright_white]\n\n"
        "[bold bright_white]INDEXA[/bold bright_white]\n"
        "[bold bright_cyan]Tecnologia que organiza informações e conecta conhecimentos.[/bold bright_cyan]",
        title="[bold bright_cyan]ENCERRANDO O SISTEMA[/bold bright_cyan]",border_style="bright_blue",padding=(1, 3),width=75))



def exibirSobre():
    console.print(Panel( "[bold bright_cyan]INDEXA[/bold bright_cyan]\n"
        "[bright_white]TECNOLOGIA E INFORMAÇÃO[bright_white]\n\n"
        "[bold bright_cyan]ACERVO[/bold bright_cyan]\n"
        "[bright_white]Sistema de Gestão de Biblioteca[/bright_white]\n\n"

        "[bold bright_cyan]NOSSA HISTÓRIA[/bold bright_cyan]\n"
        "[bright_white]A INDEXA nasceu da ideia de que a tecnologia pode transformar a maneira como as pessoas acessam, organizam e compartilham o conhecimento. Criada por um grupo de universitários, surgiu com o propósito de desenvolver soluções digitais que facilitem o dia a dia das instituições e contribuam para uma gestão mais eficiente da informação.[/bright_white]\n\n"

        "[bold bright_cyan]SOBRE O SISTEMA[/bold bright_cyan]\n"
        "[bright_white]O ACERVO facilita a organização e o gerenciamento de bibliotecas, permitindo o controle de livros, usuários e empréstimos de forma simples e eficiente.[/bright_white]\n\n"

        "[bold bright_cyan]FUNCIONALIDADES[/bold bright_cyan]\n"
        "[bright_white]• Consulta ao acervo de livros\n"
        "• Gerenciamento de empréstimos\n"
        "• Renovação de empréstimos\n"
        "• Controle de prazos e multas[/bright_white]\n\n"

        "[bold bright_cyan]NOSSA MISSÃO[/bold bright_cyan]\n"
        "[bright_white]Utilizar a tecnologia para aproximar as pessoas do conhecimento, oferecendo soluções práticas, seguras e eficientes. Acreditamos que cada livro guarda uma história e que a tecnologia pode ajudar essas histórias a chegarem cada vez mais longe.[/bright_white]\n\n"

        "[bold bright_cyan]EQUIPE E RESPONSABILIDADES[/bold bright_cyan]\n"
        "[bright_white]Rayane Reis - Desenvolvedora\n"
        "Kaua Thramn - Analista de Sistemas\n"
        "Claudio Bispo - Testador\n"
        "Patrick Campos - Gerente de Projeto e Integrador[/bright_white]\n\n"

        "[bold bright_cyan]INDEXA: tecnologia que organiza informações e conecta conhecimentos.[/bold bright_cyan]",

        title="[bold bright_cyan]SOBRE O INDEXA ACERVO[/bold bright_cyan]",
        border_style="bright_blue",
        padding=(1, 3),
        width=75))


def aguardarVolta():
    while True:
        opcao = console.input("\n[bold bright_cyan]Digite 0 para voltar ao menu:[/] ")

        if opcao == "0":
            break
        else:
            console.print("[bold bright_red]Digite 0 para voltar.[/]")

if __name__ == "__main__":
    principal()

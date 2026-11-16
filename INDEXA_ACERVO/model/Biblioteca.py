from model.Livro import Livro
from model.Cliente import Cliente
from model.Bibliotecario import Bibliotecario
from model.Emprestimo import Emprestimo
from rich.console import Console
from rich.table import Table
console = Console()

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__emprestimos = []
        self.__usuarios = []

    def getLivros(self):
        return self.__livros

    def getEmprestimos(self):
        return self.__emprestimos

    def addLivro(self, livro):
        self.__livros.append(livro)

    def removeLivro(self, livro):
        self.__livros.remove(livro)

    def addEmprestimo(self, emprestimo):
        self.__emprestimos.append(emprestimo)

    def removeEmprestimo(self, emprestimo):
        self.__emprestimos.remove(emprestimo)

    def buscarLivro(self, codigo):
        for livro in self.__livros:
            if livro.getCodigo() == codigo:
                return livro
        return None

    def buscarEmprestimo(self, codigo):
        for emprestimo in self.__emprestimos:
            if emprestimo.getCodigo() == codigo:
                return emprestimo
        return None

    def listarLivros(self):
        tabela = Table(title="ACERVO DE LIVROS", border_style="bright_blue",show_lines=True,padding=(1, 2))
        tabela.add_column("Código", style="bright_cyan")
        tabela.add_column("Título", style="bright_white")
        tabela.add_column("Autor", style="bright_white")

        for livro in self.__livros:
            tabela.add_row( livro.getCodigo(),livro.getTitulo(),livro.getAutor())
        console.print()
        console.print(tabela)
        console.print()


    def listarEmprestimos(self):
        tabela = Table(title="EMPRÉSTIMOS", border_style="bright_blue")
        tabela.add_column("Código", style="bright_cyan")
        tabela.add_column("Cliente", style="bright_white")
        tabela.add_column("Livros", justify="center")
        tabela.add_column("Renovações", justify="center")
        tabela.add_column("Data do Empréstimo")
        tabela.add_column("Data de Devolução")
        tabela.add_column("Multa", style="bright_red")

        for emprestimo in self.__emprestimos:
            tabela.add_row(
                emprestimo.getCodigo(),
                emprestimo.getCliente().getNome(),
                str(len(emprestimo.getLivros())),
                f"{emprestimo.getQuantidadeRenovacoes()}/2",
                emprestimo.getDataEmprestimo().strftime("%d/%m/%Y"),
                emprestimo.getDataDevolucao().strftime("%d/%m/%Y"),
                f"R$ {emprestimo.calcularMulta():.2f}")
        console.print(tabela)



    def carregarLivros(self):
        try:
            with open("livros.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    if len(dados) == 3:
                        self.addLivro(Livro(dados[0], dados[1], dados[2]))
        except FileNotFoundError:
            console.print("[bold bright_red]Arquivo de livros não encontrado.[/]")
        except Exception as erro:
            console.print(f"[bold bright_red]Erro ao carregar livros: {erro}[/]")
        finally:
            console.print("[bright_cyan]Carregamento de livros finalizado.[/]\n")



    def salvarLivros(self):
        try:
            with open("livros.txt", "w", encoding="utf-8") as arquivo:
                for livro in self.__livros:
                    arquivo.write(f"{livro.getCodigo()};{livro.getTitulo()};{livro.getAutor()}\n")
        except Exception as erro:
            console.print(f"[bold bright_red]Erro ao salvar livros: {erro}[/]")





    def carregarUsuarios(self):
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    if len(dados) == 5:
                        if dados[2] == "Cliente":
                            usuario = Cliente(*dados)
                        elif dados[2] == "Bibliotecario":
                            usuario = Bibliotecario(*dados)
                        else:
                            continue
                        self.__usuarios.append(usuario)
        except FileNotFoundError:
            console.print("[bold bright_red]Arquivo de usuários não encontrado.[/]")
        except Exception as erro:
            console.print(f"[bold bright_red]Erro ao carregar usuários: {erro}[/]")




    def autenticarUsuario(self, login, senha):
        for usuario in self.__usuarios:
            if usuario.getLogin() == login and usuario.getSenha() == senha:
                return usuario
        return None



    def salvarUsuarios(self):
        try:
            with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
                for usuario in self.__usuarios:
                    arquivo.write(f"{usuario.getCodigo()};{usuario.getNome()};{usuario.getTipo()};{usuario.getLogin()};{usuario.getSenha()}\n")
        except Exception as erro:
            console.print(f"[bold bright_red]Erro ao salvar usuários: {erro}[/]")



    def carregarEmprestimos(self):
        try:
            with open("emprestimos.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    if len(dados) < 4 or len(dados) > 5:
                        continue
                    codigo, codigoCliente, data, codigosLivros = dados[:4]
                    quantidadeRenovacoes = int(dados[4]) if len(dados) == 5 else 0
                    cliente = None

                    for usuario in self.__usuarios:
                        if usuario.getCodigo() == codigoCliente and isinstance(usuario, Cliente):
                            cliente = usuario
                            break

                    livros = []
                    for codigoLivro in codigosLivros.split(","):
                        livro = self.buscarLivro(codigoLivro)
                        if livro is not None:
                            livros.append(livro)

                    if cliente is not None and 1 <= len(livros) <= 3:
                        emprestimo = Emprestimo(codigo, cliente, livros, data, quantidadeRenovacoes)
                        self.addEmprestimo(emprestimo)

        except FileNotFoundError:
            console.print("[bold bright_red]Arquivo de empréstimos não encontrado.[/]")
        except Exception as erro:
            console.print(f"[bold bright_red]Erro ao carregar empréstimos: {erro}[/]")
        finally:
            console.print("[bright_cyan]Leitura de empréstimo concluída.[/]")




    def salvarEmprestimos(self):
        try:
            with open("emprestimos.txt", "w", encoding="utf-8") as arquivo:
                for emprestimo in self.__emprestimos:
                    codigos = [livro.getCodigo() for livro in emprestimo.getLivros()]
                    livros = ",".join(codigos)
                    arquivo.write(
                        f"{emprestimo.getCodigo()};{emprestimo.getCliente().getCodigo()};{emprestimo.getDataEmprestimo().strftime('%d/%m/%Y')};{livros};{emprestimo.getQuantidadeRenovacoes()}\n")
        except Exception as erro:
            console.print(f"[bold bright_red]Erro ao salvar empréstimos: {erro}[/]")



    def listarEmprestimosCliente(self, cliente):
        tabela = Table(title="MEUS EMPRÉSTIMOS", border_style="bright_blue")
        tabela.add_column("Código", style="bright_cyan")
        tabela.add_column("Livros", justify="center")
        tabela.add_column("Renovações", justify="center")
        tabela.add_column("Data do Empréstimo")
        tabela.add_column("Data de Devolução")
        tabela.add_column("Multa", style="bright_red")

        for emprestimo in self.__emprestimos:
            if emprestimo.getCliente().getCodigo() == cliente.getCodigo():
                tabela.add_row(
                    emprestimo.getCodigo(),
                    str(len(emprestimo.getLivros())),
                    f"{emprestimo.getQuantidadeRenovacoes()}/2",
                    emprestimo.getDataEmprestimo().strftime("%d/%m/%Y"),
                    emprestimo.getDataDevolucao().strftime("%d/%m/%Y"),
                    f"R$ {emprestimo.calcularMulta():.2f}")
        console.print(tabela)



    def renovarEmprestimo(self, codigo, cliente):
        emprestimo = self.buscarEmprestimo(codigo)

        if emprestimo is None:
            console.print("[bold bright_red]✗ Empréstimo não encontrado.[/]")

        elif emprestimo.getCliente().getCodigo() != cliente.getCodigo():
            console.print("[bold bright_red]✗ Esse empréstimo não pertence a você.[/]")

        elif emprestimo.renovar():
            self.salvarEmprestimos()
            data = emprestimo.getDataDevolucao().strftime("%d/%m/%Y")
            console.print("\n[bold bright_green]✓ Renovação confirmada com sucesso![/]")
            console.print(f"[bold bright_cyan]Nova data de devolução: {data}[/]")

        else:
            console.print("[bold bright_red]✗ Esse empréstimo não pode ser renovado.[/]")

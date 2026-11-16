from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, codigo, cliente, livros, dataEmprestimo, quantidadeRenovacoes=0):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__livros = livros
        self.__dataEmprestimo = datetime.strptime(dataEmprestimo, "%d/%m/%Y")
        self.__quantidadeRenovacoes = int(quantidadeRenovacoes)

        if not 1 <= len(livros) <= 3:
            raise ValueError("O empréstimo deve ter de 1 a 3 livros.")

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCliente(self):
        return self.__cliente

    def setCliente(self, cliente):
        self.__cliente = cliente

    def getLivros(self):
        return self.__livros

    def setLivros(self, livros):
        self.__livros = livros

    def getDataEmprestimo(self):
        return self.__dataEmprestimo

    def getQuantidadeRenovacoes(self):
        return self.__quantidadeRenovacoes

    def getDataDevolucao(self):
        dias = 14 + (14 * self.__quantidadeRenovacoes)
        return self.__dataEmprestimo + timedelta(days=dias)

    def podeRenovar(self):
        hoje = datetime.now().date()
        devolucao = self.getDataDevolucao().date()

        return self.__quantidadeRenovacoes < 2 and hoje <= devolucao

    def renovar(self):
        if self.podeRenovar():
            self.__quantidadeRenovacoes += 1
            return True
        return False

    def calcularMulta(self):
        hoje = datetime.now().date()
        devolucao = self.getDataDevolucao().date()

        if hoje > devolucao:
            atraso = (hoje - devolucao).days
            return atraso * len(self.__livros) * 1.50
        return 0.0

    def __str__(self):
        return f"Código: {self.__codigo} | Cliente: {self.__cliente.getNome()} | Livros: {len(self.__livros)} | Empréstimo: {self.__dataEmprestimo.strftime('%d/%m/%Y')} | Devolução: {self.getDataDevolucao().strftime('%d/%m/%Y')}"

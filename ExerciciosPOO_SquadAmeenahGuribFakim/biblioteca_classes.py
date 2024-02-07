# GERENCIAMENTO DE BIBLIOTECA


class Pessoa:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome  # público
        self._telefone = telefone  # protegido
        self._nacionalidade = nacionalidade  # protegido

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self._telefone}, Nacionalidade: {self._nacionalidade}"


class Usuario(Pessoa):
    pass


class Autor(Pessoa):
    def __init__(self, name, telefone, nacionalidade, email):
        super().__init__(name, telefone, nacionalidade)
        self.email = email


class Livro:
    def __init__(
        self,
        id,
        titulo,
        editora,
        autores,
        generos,
        exemplaresEmprestados,
    ):
        self.id = id
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.autores = autores
        self.maxRenovacao = 0
        self.exemplaresDisponiveis = 5
        self.exemplaresEmprestados = exemplaresEmprestados
        self.emprestado = False

    def emprestimo(self):
        if self.exemplaresDisponiveis > 0:
            self.exemplaresDisponiveis -= 1
            self.exemplaresEmprestados += 1
        else:
            print("Não há exemplares disponíveis para empréstimo no momento.")

    def devolucao(self):
        if self.exemplaresEmprestados > 0:
            self.exemplaresDisponiveis += 1
            self.exemplaresEmprestados -= 1
        else:
            print("Todos os exemplares foram devolvidos.")

    def renovacao(self):
        if self.maxRenovacao < 3:
            self.maxRenovacao += 1
        else:
            print("O livro não pode mais ser renovado.")

    def livro_emprestado(self):
        self.emprestado = True

    def livro_devolvido(self):
        self.emprestado = False

    def __str__(self):
        return f"Título: '{self.titulo}'\nExemplares disponíveis: {self.exemplaresDisponiveis}\nNúmero de renovações: { self.maxRenovacao}"

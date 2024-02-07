class Pessoa:
    def __init__(self, nome, telefone, nacionalidade):
        if not nome:
            raise ValueError("Nome deve ser informado.")
        if not telefone:
            raise ValueError("Telefone deve ser informado.")
        if not nacionalidade:
            raise ValueError("Nacionalidade deve ser informada.")
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.nacionalidade}"


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
        maxRenovacao,
        exemplaresDisponiveis,
        exemplaresEmprestados,
    ):
        self.id = id
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.autores = autores
        self.maxRenovacao = maxRenovacao
        self.exemplaresDisponiveis = exemplaresDisponiveis
        self.exemplaresEmprestados = exemplaresEmprestados

    def emprestimo(self):
        if self.exemplaresDisponiveis > 0:
            self.exemplaresDisponiveis -= 1
            self.exemplaresEmprestados += 1
        else:
            print("Não há exemplares disponíveis para empréstimo no momento.")

    def devolucao(self):
        if self.exemplaresEmprestadas > 0:
            self.exemplaresDisponiveis += 1
            self.exemplaresEmprestadas -= 1
        else:
            print("Todos os exemplares foram devolvidos.")

    def __str__(self):
        return f"Título: {self.titulo}\nExemplares disponíveis: {self.exemplaresDisponiveis}"

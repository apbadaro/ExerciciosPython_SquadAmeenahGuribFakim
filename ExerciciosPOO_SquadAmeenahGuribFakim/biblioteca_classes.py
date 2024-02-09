class Pessoa:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome  # público
        self._telefone = telefone  # protegido
        self.__nacionalidade = nacionalidade  # private

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self._telefone}\nNacionalidade: {self.__nacionalidade}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("O nome não pode ser vazio")
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        if not telefone:
            raise ValueError("O telefone não pode ser vazio")
        self._telefone = telefone

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        if not nacionalidade:
            raise ValueError("A nacionalidade não pode ser vazia")
        self._nacionalidade = nacionalidade


class Usuario(Pessoa):
    pass  # herança


class Autor(Pessoa):
    def __init__(self, nome, telefone, nacionalidade, email):
        super().__init__(nome, telefone, nacionalidade)  # herança
        self.email = email  # adiciona atributo exclusivo do autor


class Livro:
    def __init__(
        self,
        id,
        titulo,
        editora,
        autores,
        generos,
        exemplares_disponiveis,
        exemplares_emprestados,
    ):
        self.id = id
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.autores = []
        self.max_renovacao = 3
        self.exemplares_disponiveis = exemplares_disponiveis  # criar setter
        self.exemplares_emprestados = exemplares_emprestados
        self.emprestado = False

    def emprestimo(self):
        if self.exemplares_disponiveis > 0:
            self.exemplares_disponiveis -= 1
            self.exemplares_emprestados += 1
        else:
            print("Não há exemplares disponíveis para empréstimo no momento.")

    def devolucao(self):
        if self.exemplares_emprestados > 0:
            self.exemplares_disponiveis += 1
            self.exemplares_emprestados -= 1
        else:
            print("Todos os exemplares foram devolvidos.")

    def renovacao(self):
        if self.max_renovacao < 3:
            self.max_renovacao += 1
        else:
            print("O livro não pode mais ser renovado.")

    def livro_emprestado(self):
        self.emprestado = True

    def livro_devolvido(self):
        self.emprestado = False

    def __str__(self):
        return f"Título: '{self.titulo}'\nExemplares disponíveis: {self.exemplares_disponiveis}\nExemplares emprestados: {self.exemplares_emprestados}\nNúmero de renovações: {self.max_renovacao}"

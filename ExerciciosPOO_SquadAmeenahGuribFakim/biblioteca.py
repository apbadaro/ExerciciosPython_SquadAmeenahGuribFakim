from biblioteca_classes import Autor, Livro, Usuario


def main():
    # USUÁRIOS
    usuario1 = Usuario("Leia Organa", "111222333", "Alderaan")
    usuario2 = Usuario("Luke Skywalker", "444555666", "Tattooine")

    # AUTORES
    autor1 = Autor("JK Rowling", "0123456789", "Reino Unido", "jk@hogwarts.co.uk")
    autor2 = Autor(
        "Lewis Carroll", "9876543210", "Reino Unido", "carroll@rabbithole.co.uk"
    )

    # LIVROS
    livro1 = Livro(
        1,  # id
        "Harry Potter e a Pedra Filosofal",  # título
        "Mundo Mágico",  # editora
        [autor1],  # lista porque pode haver um ou mais autores
        ["Ficção, Fantasia, Infanto-juvenil"],  # gêneros
        6,  # exemplares disponíveis
        1,  # exemplares emprestados
    )
    livro2 = Livro(
        2,
        "Harry Potter e a Câmara Secreta",
        "Mundo Mágico",
        [autor1],
        ["Ficção, Fantasia, Infanto-juvenil"],
        5,
        2,
    )
    livro3 = Livro(
        3,
        "Harry Potter e o Prisioneiro de Azkaban",
        "Mundo Mágico",
        [autor1],
        ["Ficção, Fantasia, Infanto-juvenil"],
        4,
        2,
    )
    livro4 = Livro(
        4,
        "Alice Através do Espelho",
        "Lua Nova",
        [autor2],
        ["Ficção, Fantasia, Infanto-juvenil"],
        3,
        1,
    )

    # TESTANDO SAÍDAS NO TERMINAL
    print("\n( ( (  BIBLIOTECA  ) ) )\n")
    print(usuario1)
    print("--------------------------------")
    print(livro2)
    print("--------------------------------")
    print(autor1)


if __name__ == "__main__":
    main()

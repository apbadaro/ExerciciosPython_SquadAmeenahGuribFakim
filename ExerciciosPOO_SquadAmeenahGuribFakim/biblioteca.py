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
        ["Ficção, Fantasia, Infanto-juvenil"],  # exemplo de gêneros
        1,  # exemplo de exemplares emprestados
    )
    livro2 = Livro(
        2,
        "Harry Potter e a Câmara Secreta",
        "Mundo Mágico",
        [autor1],
        ["Ficção, Fantasia, Infanto-juvenil"],
        1,
    )
    livro3 = Livro(
        3,
        "Harry Potter e o Prisioneiro de Azkaban",
        "Mundo Mágico",
        [autor1],
        ["Ficção, Fantasia, Infanto-juvenil"],
        1,
    )
    livro4 = Livro(
        4,
        "Alice Através do Espelho",
        "Lua Nova",
        [autor2],
        ["Ficção, Fantasia, Infanto-juvenil"],
        3,
    )

    # TESTANDO SAÍDAS NO TERMINAL
    print("\nT E S T E S :")
    print("----------------------------")
    print(
        f"Usuário #1 aluga livros ID 2 e 3:\n{usuario1.nome.upper()} alugou '{livro2.titulo.upper()}' e '{livro3.titulo.upper()}'."
    )
    print("----------------------------")
    print(f"Usuário #1: {usuario1}")
    print("----------------------------")
    print(f"Livro #1: {livro1}")
    print("----------------------------")
    print(f"Autor #1: {autor1}")
    print()


if __name__ == "__main__":
    main()

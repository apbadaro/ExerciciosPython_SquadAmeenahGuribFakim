import sqlite3

#serve para usar python com banco de dados

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()


# cursor.execute('CREATE TABLE autor(cpf VARCHAR(11) primary key, nome VARCHAR(50), endereco VARCHAR(100), telefone INT, email VARCHAR(50));')

# cursor.execute('CREATE TABLE usuario(cpf VARCHAR(11) primary key, nome VARCHAR(50), nacionalidade VARCHAR(20), telefone INT);')


#Criar tabela com FK
# cursor.execute('''
#     CREATE TABLE livro (
#         id INT PRIMARY KEY,
#         titulo VARCHAR(50),
#         editora VARCHAR(20),
#         autores VARCHAR(11),
#         FOREIGN KEY (autores) REFERENCES autor(cpf)
#     );
# ''')

# cursor.execute('ALTER TABLE livro ADD COLUMN maxRenovacao INT')

# cursor.execute('''
#     CREATE TABLE emprestimo (
#         data_emprestimo VARCHAR(8),
#         data_devolucao VARCHAR(8),
#         estado VARCHAR(12),
#         livro_id INT,
#         FOREIGN KEY (livro_id) REFERENCES livro(id)
#     );
# ''')

# dados = cursor.execute('SELECT * FROM livro')
# for livros in dados:
#   print(livros)

# cursor.execute('INSERT INTO livro VALUES (1, "Harry Potter", "Mundo Mágico", 22222222222, 5, "ficção", 3)')
# cursor.execute('INSERT INTO livro VALUES (2, "Harry Potter e o Prisioneiro de Azkaban", "Mundo Mágico", 12345678901, 8, "ficção", 3)')
# cursor.execute('INSERT INTO livro VALUES (3, "Harry Potter e a Câmara Secreta", "Mundo Mágico", 22222222222, 12, "ficção", 3)')
# cursor.execute('INSERT INTO livro VALUES (4, "Alice através do espelho", "Lua Nova", 12345678901, 8, "ficção", 4)')

# cursor.execute('INSERT INTO autor VALUES (22222222222, "Pedro", "Salvador", 999999999, "rafa@uol.com")')


# dados = cursor.execute('SELECT * FROM livro')
# for livro in dados:
#   print(livro)

# dados = cursor.execute('SELECT titulo FROM livro WHERE autores="22222222222"')
# for livro in dados:
#   print(livro)

dados = cursor.execute('SELECT titulo, maxRenovacao FROM livro')
for livro in dados:
  print(livro)


conexao.commit()
conexao.close

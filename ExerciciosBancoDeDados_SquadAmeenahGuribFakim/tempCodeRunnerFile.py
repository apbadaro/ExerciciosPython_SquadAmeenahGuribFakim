
dados = cursor.execute('SELECT titulo, maxRenovacao FROM livro')
for livro in dados:
  print(livro)

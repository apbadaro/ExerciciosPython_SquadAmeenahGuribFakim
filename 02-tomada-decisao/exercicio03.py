nota = int(input("Informe uma nota entre 0 e 10: "))

while nota > 10 or nota < 0:
  nota = int(input("Valor informado inválido, informe novamente um valor entre 0 e 10: "))
print("Valor informado esta correto. Fim do Programa!")
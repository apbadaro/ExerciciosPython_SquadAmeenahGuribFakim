#Exercicio 6
#Solicita usuario e senha
usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

#Resultado
if usuario == "admin" and senha == "admin123" :
    print("Acesso permitido! ")
else:
    print("Usuario ou senha incorretos. Acesso negado. ")

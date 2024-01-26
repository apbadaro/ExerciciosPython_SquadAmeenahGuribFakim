#Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = {
    'Ana': '71 91345-6789',
    'Marta': '11 92765-4321',
    'Pedro': '21 91322-2333',
    'Lucas': '75 96866-6777',
    'Luis': '11 96524-5555',
    'Leonardo': '71 93333-3333'
}

def procurar_contato():
    nome_procurado = input("Digite o nome do contato que deseja procurar: ")
    
    if nome_procurado in contatos:
        print(f"O telefone de {nome_procurado} é: {contatos[nome_procurado]}")
    else:
        print("Contato não encontrado.")

procurar_contato()
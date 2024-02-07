#Exercicio 5
#Funcao
def contar_vogais(frase):
    vogais = "aeiouAEIOU"

#funcao
    total_vogais = sum(frase.count(vogal) for vogal in vogais)

    return total_vogais

#Digitar uma frase
frase_usuario = input("Digite uma frase: ")

#resultado
resultado = contar_vogais(frase_usuario)
print(f"Total de vogais na frase: {resultado}")




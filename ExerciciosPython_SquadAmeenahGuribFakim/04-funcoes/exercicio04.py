#Exercicio 4
#Funcao para calcular conversao
def moeda_estrangeira(valor_reais, taxa_conversao):
    return valor_reais / taxa_conversao

#Solicita valor em reais
valor_reais = float(input("Digite o valor em reais. "))

#Conversao
tabela_conversao = {
    'Dolar Americano': 4.91,
    'Peso Argentino': 0.02,
    'Dolar Australiano': 3.18,
    'Dolar Canadense': 3.64,
    'Franco suico': 0.42,
    'Euro': 5.36,
    'Libra': 6.21
}

#resultado
print("Valor em cada moeda estrangeira: ")
for moeda, taxa in tabela_conversao.items():
    valor_moeda_estrangeira = moeda_estrangeira(valor_reais, taxa)
    print(f"{moeda}: {valor_moeda_estrangeira: .2f}")


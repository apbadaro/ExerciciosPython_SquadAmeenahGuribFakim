
# ====================================================================
# ! EXERCÍCIO 10:
'''
10.Faça um programa que lê três números inteiros e os mostra em ordem crescente.
'''

# ? RESPOSTA:
print("Resposta do Exercício 10: ")

# Imput de Dados pelo usuário:
primeiro_num = int(input("Digite um número: "))
segundo_num = int(input("Digite mais um número: "))
terceiro_num = int(input("Agora, digite o último número: "))

# Para criar uma lista com os 3 números:
todos_numeros = [primeiro_num, segundo_num, terceiro_num]

# Ordenar a Lista (ordem crescente)
ordem_crescente = sorted(todos_numeros)

# Imprimir no Terminal:
print(f"Os números escolhidos, em ordem crescente, são {ordem_crescente}.")

'''
# RESPOSTA NO TERMINAL:

TESTE 01:
Resposta do Exercício 10: 
Digite um número: 4  
Digite mais um número: 2
Agora, digite o último número: 7
Os números escolhidos, em ordem crescente, são [2, 4, 7].

TESTE 02:
Resposta do Exercício 10: 
Digite um número: 54
Digite mais um número: 32
Agora, digite o último número: 6
Os números escolhidos, em ordem crescente, são [6, 32, 54].

TESTE 03:
Resposta do Exercício 10: 
Digite um número: -14
Digite mais um número: 4
Agora, digite o último número: 0
Os números escolhidos, em ordem crescente, são [-14, 0, 4].

'''
# fim
# ====================================================================

# ====================================================================
# ! EXERCÍCIO 09:

# ? RESPOSTA POSSÍVEL:
print("Resposta do Exercício 09: ")

# Declaração de variaveis:
numero_par = 0
numero_impar = 0

# Operações:
# Enquanto Verdade
while True:
    # try-except - lidar com erros
    try:
        # Imput de Dados pelo usuário:
        numero_digitado = int(input('Digite um número positivo ("ou 0 para sair"): '))
        # Para parar se digitado o zero
        if numero_digitado == 0:
            break
        # Para verificar se o número é positivo ou negativo
        if numero_digitado > 0:
            # Se positivo, olhar se é par ou impar e somar +1
            if numero_digitado % 2 == 0:
                numero_par += 1
            else:
                numero_impar += 1
        else:
            # Caso usuário digite numero negativo
            print("Insira apenas números positivos!")
    # Caso o usuário já insira numero negativo imediatamente 
    except ValueError:
        print("Insira apenas números positivos!")

# Imprimir no Terminal:
print(f"Total de números pares inseridos: {numero_par}.")
print(f"Total de números impares inseridos: {numero_impar}.")
        
'''
# RESPOSTA NO TERMINAL:

TESTE 01:
Resposta do Exercício 09: 
Digite um número positivo ("ou 0 para sair"): 5
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): 7
Digite um número positivo ("ou 0 para sair"): 4
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): 0
Total de números pares inseridos: 3.
Total de números impares inseridos: 2.

# TESTE 02:
Resposta do Exercício 09: 
Digite um número positivo ("ou 0 para sair"): -5
Insira apenas números positivos!
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): -3
Insira apenas números positivos!
Digite um número positivo ("ou 0 para sair"): 5
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): 3
Digite um número positivo ("ou 0 para sair"): 0
Total de números pares inseridos: 2.
Total de números impares inseridos: 2.

'''
# fim
# ====================================================================

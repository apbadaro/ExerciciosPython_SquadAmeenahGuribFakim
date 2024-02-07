print('Vamos descobrir a sua idade!')

from datetime import datetime

def calcular_idade(ano_nascimento): 
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = calcular_idade(ano_nascimento)
print(f'Você tem {idade} anos!')

'''Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou 
vice-versa. Para cada opção, crie uma função.'''

def transforma_celsius(a):
    resultado = (a * 9/5) + 32
    print(f'{a:.2f} ºC é {resultado:.2f} F')

def transforma_fahrenheit(a):
    resultado = (a - 32) * 5/9
    print(f'{a:.2f} F é {resultado:.2f} ºC')

print('Se liga no menu:')
print('1 - Transformar em celsius;')
print('2 - Transformar em fahrenheit;')
print('0 - Encerrar programa.')
opcao = int(input('Selecione uma opção: '))
while opcao != 0:
    if opcao == 1:
        transforma_celsius(a=float(input('Digite uma temperatura: ')))
        opcao = int(input('Selecione uma opção: '))
    elif opcao == 2:
        transforma_fahrenheit(a=float(input('Digite uma temperatura: ')))
        opcao = int(input('Selecione uma opção: '))
    else:
        print('Opção inválida.')
        opcao = int(input('Selecione uma opção: '))
print('Fim do programa.')

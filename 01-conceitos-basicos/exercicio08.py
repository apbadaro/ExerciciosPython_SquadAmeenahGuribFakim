# Faça um programa que pergunte quanto você ganha por hora e a quantidade de horas trabalhadas no mês.
# Calcule e mostre o total do salário do referido mês.

valor_hora = float(input("Digite quanto você ganha por hora: R$ "))
horas_mes = float(input("Digite a quantidade de horas trabalhadas este mês: "))
salario = valor_hora * horas_mes

print("-----------------------------")
print(f"\nEste mês seu salário foi R$ {salario:.2f}.\n")

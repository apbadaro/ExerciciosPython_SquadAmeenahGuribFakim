# Escreva um programa que calcule o salário líquido. Lembrando-se de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
# Referência: 1903,98 = isento; 1903,99 e 2826,65 = 7,5%; 2826,66 e 3751,05 = 15%; 3751,06 e 4664,68 = 22,5%; acima de 4664,68 = 27,5%

salario_bruto = float(input("Digite seu salário bruto: R$ "))

if salario_bruto <= 1903.98:
    print(f"Seu salário líquido é R$ {salario_bruto:.2f} e é isento de IR.")
elif salario_bruto >= 1908.99 and salario_bruto <= 2826.65:
    faixa2 = salario_bruto - (salario_bruto * 0.075)
    print(f"Seu salário líquido é R$ {faixa2:.2f} e sofre um desconto de 7,5%.")
elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
    faixa3 = salario_bruto - (salario_bruto * 0.15)
    print(f"Seu salário líquido é R$ {faixa3:.2f} e sofre um desconto de 15%.")
elif salario_bruto >= 3751.06 and salario_bruto <= 4664.68:
    faixa4 = salario_bruto - (salario_bruto * 0.225)
    print(f"Seu salário líquido é R$ {faixa4:.2f} e sofre um desconto de 22,5%.")
elif salario_bruto > 4664.68:
    faixa5 = salario_bruto - (salario_bruto * 0.275)
    print(f"Seu salário líquido é R$ {faixa5:.2f} e sofre um desconto de 27,5%.")

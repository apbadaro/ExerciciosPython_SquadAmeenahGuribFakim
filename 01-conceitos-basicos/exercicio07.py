# Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o IMC.
# IMC: peso / (altura x altura)

peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}.")

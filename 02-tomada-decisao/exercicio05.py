#Exercicio 5
#Solicita os lados do triangulo
lado1 = float(input("Digite o primeiro lado do triangulo. "))
lado2 = float(input("Digite o segundo lado do triangulo. "))
lado3 = float(input("Digite o terceiro lado do triangulo. "))

#Verifica os lados do triangulo
if lado1 == lado2 == lado3:
    print("O triangulo e equilatero. ")
if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triangulo e isosceles. ")
else :
    print("O triangulo e escaleno. ")

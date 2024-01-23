#Exercicio 7
#Solicita a idade do usuario
idade = float(input("Digite sua idade. "))

#Verificacao
if idade <= 12 :
    print("Voce e uma crianca. ")
if 13 <= idade < 18:
    print("Voce e um adolescente. ")
if 18 <= idade <= 65 : 
    print("Voce e um adulto. ")
if idade >= 66 :
    print("Voce e um idoso. ")
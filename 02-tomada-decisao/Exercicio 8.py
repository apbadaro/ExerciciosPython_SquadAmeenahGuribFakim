#Exercicio 8
#Solicitar 3 numeros
numero10 = float(input("Digite o primeiro numero: "))
numero11 = float(input("Digite o segundo numero: "))
numero12 = float(input("Digite o terceiro numero: "))

#Solucao 
if numero10 > numero11 and numero10 > numero12 : 
    maior_numero = numero10
if numero11 > numero10 and numero11 > numero12 :
    maior_numero = numero11
else:
    maior_numero = numero12

#Resultado
print(f"O maior numero entre {numero10}, {numero11} e {numero12} e : {maior_numero}. ")    

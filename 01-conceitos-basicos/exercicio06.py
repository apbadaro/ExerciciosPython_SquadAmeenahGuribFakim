# Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# avião = 600 km/h; carro = 100 km/h; ônibus = 80 km/h

distancia = int(input("Digite a distância em quilômetros: "))
velocidade = int(input("Digite a velocidade do veículo (km/h): "))

tempo_viagem = distancia / velocidade
tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

print("-----------------------------")
print(f"\nDuração da viagem: {tempo_viagem:.2f} horas.")
print("\nCOMPARATIVO:")
print(f"Você faria o mesmo percurso de avião em {tempo_aviao:.2f} horas.")
print(f"Você faria o mesmo percurso de carro em {tempo_carro:.2f} horas.")
print(f"Você faria o mesmo percurso de ônibus em {tempo_onibus:.2f} horas.")

horaExercicios = int(input("Informe a quantidade de horas por semana que você prática exercício físico: "))
caloriasPorMinuto = 5
caloriasGastaSemana = (horaExercicios * 60) * caloriasPorMinuto
print(f"Nesta semana você gastou {caloriasGastaSemana} calorias por ter praticado {horaExercicios} horas de exercícios")
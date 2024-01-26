# Exercício 2
notas_alunos = []

for i in range(5):
    notas = [float(input(f"Informe a nota {j + 1} do aluno {i + 1}: ")) for j in range(4)]
    media = sum(notas) / len(notas)
    notas_alunos.append(media)

alunos_aprovados = sum(1 for nota in notas_alunos if nota >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

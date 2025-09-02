alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [student for student, grade in zip(alunos, notas) if grade >= 60]

print("Aprovados:", aprovados)
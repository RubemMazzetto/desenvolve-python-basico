n = int(input("Digite a quantidade de respondentes: "))

if n <= 0:
    print("Erro! A quantidade de respondentes deve ser maior que 0.")
    exit()

total_age = 0

for i in range(n):
    age = int(input(f"Digite a idade do respondente {i + 1}: "))
    total_age += age

average_age = total_age / n

print(f"A média das idades é: {average_age:.2f}")
amount = int(input("Digite a quantia em reais: "))

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_20 = amount // 20
amount = amount % 20

notes_10 = amount // 10
amount = amount % 10

notes_5 = amount // 5
amount = amount % 5

notes_2 = amount // 2
amount = amount % 2

notes_1 = amount

print(f"{notes_100} nota(s) de R$100,00")
print(f"{notes_50} nota(s) de R$50,00")
print(f"{notes_20} nota(s) de R$20,00")
print(f"{notes_10} nota(s) de R$10,00")
print(f"{notes_5} nota(s) de R$5,00")
print(f"{notes_2} nota(s) de R$2,00")
print(f"{notes_1} nota(s) de R$1,00")
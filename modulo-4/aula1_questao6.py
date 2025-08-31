n = int(input())

total_guinea_pigs = 0
frogs = 0
rats = 0
rabbits = 0

for _ in range(n):
    line = input()
    quantity, cobaia_type = map(str, line.split())
    quantity = int(quantity)

    total_guinea_pigs += quantity
    if cobaia_type == 'S':
        frogs += quantity
    elif cobaia_type == 'R':
        rats += quantity
    elif cobaia_type == 'C':
        rabbits += quantity

percent_frogs = (frogs / total_guinea_pigs) * 100
percent_rats = (rats / total_guinea_pigs) * 100
percent_rabbits = (rabbits / total_guinea_pigs) * 100

print(f"Total: {total_guinea_pigs} cobaias")
print(f"Total de coelhos: {rabbits}")
print(f"Total de ratos: {rats}")
print(f"Total de sapos: {frogs}")
print(f"Percentual de coelhos: {percent_rabbits:.2f} %")
print(f"Percentual de ratos: {percent_rats:.2f} %")
print(f"Percentual de sapos: {percent_frogs:.2f} %")
import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

contagem = {}
for num in set(lista1) | set(lista2):
    contagem[num] = (lista1.count(num), lista2.count(num))

print("lista1:", lista1)
print("lista2:", lista2)
print("Interseccao:", interseccao)
print("Contagem:")
for num, (count1, count2) in contagem.items():
    if count1 > 0 or count2 > 0: 
        print(f"{num}: (lista1={count1}, lista2={count2})")
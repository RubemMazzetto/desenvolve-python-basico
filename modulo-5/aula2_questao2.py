import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

total = sum(elementos)
media = total / num_elementos

print("Lista elementos:", elementos)
print("Soma dos valores da lista:", total)
print("Média dos valores da lista:", round(media, 2))
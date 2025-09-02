import random
import math

n = int(input("Digite o valor de n: "))

if n <= 0:
    print("Erro! n deve ser positivo.")
    exit()

total = sum(random.randint(0, 100) for _ in range(n))

result = round(math.sqrt(total), 2)

print(f"A raiz quadrada da soma dos {n} valores é: {result}")
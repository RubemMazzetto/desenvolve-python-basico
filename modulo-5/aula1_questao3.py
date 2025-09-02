import random

target = random.randint(1, 10)

while True:
    guess = int(input("Adivinhe o número entre 1 e 10: "))
    if guess == target:
        print(f"Correto! O número é {guess}.")
        break
    elif guess < target:
        print("Muito baixo, tente novamente!")
    else:
        print("Muito alto, tente novamente!")
import random

def print_hangman(errors):
    """Imprime o estágio do enforcado baseado no número de erros."""
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as file:
        stages = file.read().split('\n\n')
    print(stages[min(errors, len(stages) - 1)])

with open("gabarito_forca.txt", "r", encoding="utf-8") as file:
    words = file.read().splitlines()
secret_word = random.choice(words).lower()
guessed = ["_" for _ in secret_word]
errors = 0
max_errors = 6

while errors < max_errors and "_" in guessed:
    print(" ".join(guessed))
    guess = input("Digite uma letra: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Digite uma única letra válida.")
        continue
    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed[i] = guess
    else:
        errors += 1
        print_hangman(errors)
    print()

if "_" not in guessed:
    print(f"Parabéns! A palavra era {secret_word}.")
else:
    print_hangman(errors)
    print(f"Game Over! A palavra era {secret_word}.")
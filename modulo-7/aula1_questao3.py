def count_spaces(phrase):
    """Conta o número de espaços em branco em uma frase."""
    return sum(1 for char in phrase if char.isspace())

# Programa principal
user_phrase = input("Digite a frase: ")
space_count = count_spaces(user_phrase)
print(f"Espaços em branco: {space_count}")
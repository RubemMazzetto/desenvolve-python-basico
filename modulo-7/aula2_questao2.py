def replace_vowels(phrase):
    """Substitui todas as vogais por '*' na frase."""
    vowels = "aeiouAEIOU"
    return ''.join('*' if char in vowels else char for char in phrase)

user_phrase = input("Digite uma frase: ")
modified_phrase = replace_vowels(user_phrase)
print(f"Frase modificada: {modified_phrase}")
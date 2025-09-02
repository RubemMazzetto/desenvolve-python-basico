def count_vowels(phrase):
    """Conta vogais e retorna sua quantidade e índices."""
    vowels = "aeiouAEIOU"
    vowel_indices = [i for i, char in enumerate(phrase) if char in vowels]
    return len(vowel_indices), vowel_indices

user_phrase = input("Digite uma frase: ")
count, indices = count_vowels(user_phrase)
print(f"{count} vogais")
print(f"Índices {indices}")
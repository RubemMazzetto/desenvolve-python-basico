phrase = input("Digite uma frase: ")

vowels = "aeiouAEIOU"

vowel_list = sorted([char for char in phrase if char in vowels])  # Vogais ordenadas
consonant_list = [char for char in phrase if char not in vowels and char.strip()]  # Consoantes, sem espaços

print("Vogais:", vowel_list)
print("Consoantes:", consonant_list)
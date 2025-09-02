def find_anagrams(phrase, target):
    """Encontra todos os anagramas da palavra objetivo na frase."""
    target_sorted = ''.join(sorted(target.lower()))
    words = phrase.split()
    anagrams = [word for word in words if len(word) == len(target) and 
                ''.join(sorted(word.lower())) == target_sorted]
    return anagrams

user_phrase = input("Digite uma frase: ")
target_word = input("Digite a palavra objetivo: ")
anagrams = find_anagrams(user_phrase, target_word)
print(f"Anagramas: {anagrams}")
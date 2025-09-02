def process_phrase_to_words():
    """Lê 'frase.txt', remove não-alfabéticos e salva em 'palavras.txt'."""
    with open("frase.txt", "r", encoding="utf-8") as input_file:
        phrase = input_file.read()
    words = [''.join(char for char in word if char.isalpha()) for word in phrase.split()]
    with open("palavras.txt", "w", encoding="utf-8") as output_file:
        output_file.write('\n'.join(words))
    with open("palavras.txt", "r", encoding="utf-8") as output_file:
        return output_file.read()

content = process_phrase_to_words()
print(content)
import os

def save_phrase_to_file(phrase):
    """Salva a frase em um arquivo 'frase.txt' e retorna o caminho completo."""
    file_path = os.path.join(os.getcwd(), "frase.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(phrase)
    return file_path

user_phrase = input("Digite uma frase: ")
file_path = save_phrase_to_file(user_phrase)
print(f"Frase salva em {file_path}")
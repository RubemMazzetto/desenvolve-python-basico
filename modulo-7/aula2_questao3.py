def is_palindrome(phrase):
    """Verifica se a frase é um palíndromo, ignorando espaços e pontuação."""
    cleaned = ''.join(char.lower() for char in phrase if char.isalnum())
    return cleaned == cleaned[::-1]

while True:
    user_phrase = input('Digite uma frase (digite "fim" para encerrar): ')
    if user_phrase.lower() == "fim":
        break
    result = "é palíndromo" if is_palindrome(user_phrase) else "não é palíndromo"
    print(f'"{user_phrase}" {result}')
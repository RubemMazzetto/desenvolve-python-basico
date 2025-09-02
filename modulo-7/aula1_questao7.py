import random

def encrypt(names):
    """Criptografa uma lista de strings com deslocamento aleatório."""
    shift = random.randint(1, 10)
    encrypted_names = [''.join(chr((ord(c) - 33 + shift) % 94 + 33) 
                           for c in name) for name in names]
    return encrypted_names, shift

names = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

encrypted_names, key = encrypt(names)
print(f"chave_aleatoria = {key}")
print(f"nomes_cript = {encrypted_names}")
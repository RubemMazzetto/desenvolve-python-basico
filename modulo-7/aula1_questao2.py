def greet_user(first_name, last_name):
    """Concatena nome e sobrenome e retorna mensagem de boas-vindas."""
    full_name = f"{first_name} {last_name}"
    return f"Bem-vinda, {full_name}!"

first_name = input("Digite seu primeiro nome: ")
last_name = input("Digite seu sobrenome: ")
print(greet_user(first_name, last_name))
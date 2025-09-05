from entities.user import User

def create_user(users, username, password, role):
    """
    Cria um novo usuário.
    Entrada: Lista de usuários, username, password, role.
    Saída: True se criado, False se já existe.
    """
    if any(u.username == username for u in users):
        return False
    users.append(User(username, password, role))
    return True

def read_users(users):
    """
    Retorna lista de usuários.
    Entrada: Lista de usuários.
    Saída: Lista de usuários.
    """
    return users

def update_user(users, username, new_password=None, new_role=None):
    """
    Atualiza um usuário.
    Entrada: Lista de usuários, username, novos valores opcionais.
    Saída: True se atualizado, False se não encontrado.
    """
    for user in users:
        if user.username == username:
            if new_password:
                user.password = new_password
            if new_role:
                user.role = new_role
            return True
    return False

def delete_user(users, username):
    """
    Deleta um usuário.
    Entrada: Lista de usuários, username.
    Saída: True se deletado, False se não encontrado.
    """
    original_length = len(users)
    users[:] = [u for u in users if u.username != username]
    return len(users) < original_length
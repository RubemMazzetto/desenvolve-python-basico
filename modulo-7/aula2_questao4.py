def validate_password(password):
    """Valida se a senha atende a todos os critérios de segurança."""
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)
    return has_upper and has_lower and has_digit and has_special

password1 = "Senha123@"
password2 = "senhafraca"
password3 = "Senha_fraca"
print(validate_password(password1))  # True
print(validate_password(password2))  # False
print(validate_password(password3))  # False
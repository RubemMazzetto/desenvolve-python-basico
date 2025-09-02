def calculate_check_digit(numbers, multipliers):
    """Calcula o dígito verificador."""
    total = sum(n * m for n, m in zip(numbers, multipliers))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder

def validate_cpf(cpf):
    """Valida um CPF no formato XXX.XXX.XXX-XX."""
    cleaned_cpf = cpf.replace(".", "").replace("-", "")
    if len(cleaned_cpf) != 11 or not cleaned_cpf.isdigit():
        return "Inválido"

    digits = [int(d) for d in cleaned_cpf[:9]]
    check_digits = [int(d) for d in cleaned_cpf[9:]]

    first_check = calculate_check_digit(digits, range(10, 1, -1))
    if first_check != check_digits[0]:
        return "Inválido"

    digits.append(first_check)
    second_check = calculate_check_digit(digits, range(11, 1, -1))
    if second_check != check_digits[1]:
        return "Inválido"

    return "Válido"

user_cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
result = validate_cpf(user_cpf)
print(result)
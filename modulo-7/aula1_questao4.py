def format_phone_number(phone):
    phone_str = str(phone).replace("-", "")
    if len(phone_str) == 8:
        phone_str = "9" + phone_str
    elif len(phone_str) == 9 and phone_str[0] != "9":
        return "Número inválido: deve começar com 9 se tiver 9 dígitos."
    if len(phone_str) != 9:
        return "Número inválido: deve ter 8 ou 9 dígitos."
    return f"{phone_str[:5]}-{phone_str[5:]}"

user_phone = input("Digite o número: ")
formatted_phone = format_phone_number(user_phone)
print(f"Número completo: {formatted_phone}")
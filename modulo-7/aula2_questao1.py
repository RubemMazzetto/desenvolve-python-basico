def format_birth_date(date_str):
    """Converte data de nascimento para formato com mês por extenso."""
    months = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    day, month, year = map(int, date_str.split('/'))
    return f"{day} de {months[month - 1]} de {year}"

birth_date = input("Digite uma data de nascimento (dd/mm/aaaa): ")
formatted_date = format_birth_date(birth_date)
print(f"Você nasceu em {formatted_date}.")
def analyze_script():
    """Analisa o arquivo 'estomago.txt' e retorna estatísticas."""
    with open("estomago.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("Primeiras 25 linhas:")
    for line in lines[:25]:
        print(line.strip())

    print(f"\nNúmero de linhas: {len(lines)}")

    longest_line = max(lines, key=len)
    print(f"Linha com maior número de caracteres: {longest_line.strip()}")

    nonato_count = sum(1 for line in lines if " Nonato" in line or " nonato" in line)
    iria_count = sum(1 for line in lines if " Íria" in line or " íria" in line)
    print(f"Menção a 'Nonato': {nonato_count}")
    print(f"Menção a 'Íria': {iria_count}")

analyze_script()
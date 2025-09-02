def create_book_csv():
    """Cria um arquivo CSV com informações de livros."""
    books = [
        ["O Caçador de Pipas", "Khaled Hosseini", "2003", "368"],
        ["Torto Arado", "Itamar Vieira Junior", "2019", "264"],
        ["1984", "George Orwell", "1949", "328"],
        ["Dom Casmurro", "Machado de Assis", "1899", "256"],
        ["O Senhor dos Anéis", "J.R.R. Tolkien", "1954", "1178"],
        ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", "1997", "223"],
        ["Cem Anos de Solidão", "Gabriel García Márquez", "1967", "417"],
        ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "96"],
        ["A Culpa é das Estrelas", "John Green", "2012", "288"],
        ["Sapiens", "Yuval Noah Harari", "2011", "443"]
    ]
    with open("meus_livros.csv", "w", encoding="utf-8") as file:
        file.write("Título,Autor,Ano de publicação,Número de páginas\n")
        for book in books:
            file.write(",".join(book) + "\n")

create_book_csv()
print("Arquivo 'meus_livros.csv' criado com sucesso.")
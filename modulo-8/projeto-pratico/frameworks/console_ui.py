from entities.user import User
from entities.product import Product

def login(users):
    """
    Realiza o login.
    Entrada: Lista de usuários.
    Saída: User logado ou None.
    """
    username = input("Username: ")
    password = input("Password: ")
    for user in users:
        if user.username == username and user.password == password:
            return user
    print("Login inválido.")
    return None

def print_users(users):
    """
    Imprime lista de usuários.
    Entrada: Lista de usuários.
    """
    for user in users:
        print(f"Username: {user.username}, Role: {user.role}")

def print_products(products):
    """
    Imprime lista de produtos.
    Entrada: Lista de produtos.
    """
    for prod in products:
        print(f"ID: {prod.id}, Nome: {prod.name}, Preço: {prod.price}, Quantidade: {prod.quantity}")

def admin_menu(users, products, user_repo, product_repo):
    """
    Menu para admin.
    """
    from use_cases.user_use_cases import create_user, update_user, delete_user
    from use_cases.product_use_cases import create_product, update_product, delete_product, search_product, get_products_sorted_by_name, get_products_sorted_by_price

    while True:
        print("\nAdmin Menu:")
        print("1. CRUD Usuários")
        print("2. CRUD Produtos")
        print("3. Buscar Produto")
        print("4. Listar Produtos por Nome")
        print("5. Listar Produtos por Preço")
        print("6. Logout")
        choice = input("Escolha: ")

        if choice == '1':
            user_crud_menu(users, user_repo)
        elif choice == '2':
            product_crud_menu(products, product_repo)
        elif choice == '3':
            query = input("Buscar por nome ou ID: ")
            found = search_product(products, query)
            if found:
                print_products(found)
            else:
                print("Produto não encontrado.")
        elif choice == '4':
            sorted_prods = get_products_sorted_by_name(products)
            print_products(sorted_prods)
        elif choice == '5':
            sorted_prods = get_products_sorted_by_price(products)
            print_products(sorted_prods)
        elif choice == '6':
            break
        else:
            print("Opção inválida.")

def cliente_menu(products):
    """
    Menu para cliente.
    """
    from use_cases.product_use_cases import search_product, get_products_sorted_by_name, get_products_sorted_by_price

    while True:
        print("\nCliente Menu:")
        print("1. Listar Produtos")
        print("2. Buscar Produto")
        print("3. Listar Produtos por Nome")
        print("4. Listar Produtos por Preço")
        print("5. Logout")
        choice = input("Escolha: ")

        if choice == '1':
            print_products(products)
        elif choice == '2':
            query = input("Buscar por nome ou ID: ")
            found = search_product(products, query)
            if found:
                print_products(found)
            else:
                print("Produto não encontrado.")
        elif choice == '3':
            sorted_prods = get_products_sorted_by_name(products)
            print_products(sorted_prods)
        elif choice == '4':
            sorted_prods = get_products_sorted_by_price(products)
            print_products(sorted_prods)
        elif choice == '5':
            break
        else:
            print("Opção inválida.")

def user_crud_menu(users, user_repo):
    """
    Submenu CRUD usuários.
    """
    from use_cases.user_use_cases import create_user, read_users, update_user, delete_user

    while True:
        print("\nCRUD Usuários:")
        print("1. Criar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Voltar")
        choice = input("Escolha: ")

        if choice == '1':
            username = input("Novo username: ")
            password = input("Nova password: ")
            role = input("Role (admin/cliente): ")
            if create_user(users, username, password, role):
                user_repo.save_users(users)
                print("Usuário criado.")
            else:
                print("Username já existe.")
        elif choice == '2':
            print_users(read_users(users))
        elif choice == '3':
            username = input("Username a atualizar: ")
            new_password = input("Nova password (deixe vazio para manter): ") or None
            new_role = input("Nova role (deixe vazio para manter): ") or None
            if update_user(users, username, new_password, new_role):
                user_repo.save_users(users)
                print("Usuário atualizado.")
            else:
                print("Usuário não encontrado.")
        elif choice == '4':
            username = input("Username a deletar: ")
            if delete_user(users, username):
                user_repo.save_users(users)
                print("Usuário deletado.")
            else:
                print("Usuário não encontrado.")
        elif choice == '5':
            break
        else:
            print("Opção inválida.")

def product_crud_menu(products, product_repo):
    """
    Submenu CRUD produtos.
    """
    from use_cases.product_use_cases import create_product, read_products, update_product, delete_product

    while True:
        print("\nCRUD Produtos:")
        print("1. Criar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Voltar")
        choice = input("Escolha: ")

        if choice == '1':
            name = input("Nome do livro: ")
            price = float(input("Preço: "))
            quantity = int(input("Quantidade: "))
            create_product(products, name, price, quantity)
            product_repo.save_products(products)
            print("Produto criado.")
        elif choice == '2':
            print_products(read_products(products))
        elif choice == '3':
            product_id = input("ID do produto a atualizar: ")
            new_name = input("Novo nome (deixe vazio para manter): ") or None
            new_price_str = input("Novo preço (deixe vazio para manter): ")
            new_price = float(new_price_str) if new_price_str else None
            new_quantity_str = input("Nova quantidade (deixe vazio para manter): ")
            new_quantity = int(new_quantity_str) if new_quantity_str else None
            if update_product(products, product_id, new_name, new_price, new_quantity):
                product_repo.save_products(products)
                print("Produto atualizado.")
            else:
                print("Produto não encontrado.")
        elif choice == '4':
            product_id = input("ID do produto a deletar: ")
            if delete_product(products, product_id):
                product_repo.save_products(products)
                print("Produto deletado.")
            else:
                print("Produto não encontrado.")
        elif choice == '5':
            break
        else:
            print("Opção inválida.")
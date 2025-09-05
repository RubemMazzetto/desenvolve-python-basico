from adapters.user_repository import UserRepository
from adapters.product_repository import ProductRepository
from frameworks.console_ui import login, admin_menu, cliente_menu

def main():
    user_repo = UserRepository()
    product_repo = ProductRepository()
    
    users = user_repo.load_users()
    products = product_repo.load_products()
    
    while True:
        user = login(users)
        if user:
            if user.role == 'admin':
                admin_menu(users, products, user_repo, product_repo)
            elif user.role == 'cliente':
                cliente_menu(products)
            else:
                print("Role desconhecida.")
        else:
            retry = input("Tentar novamente? (s/n): ")
            if retry.lower() != 's':
                break

if __name__ == "__main__":
    main()
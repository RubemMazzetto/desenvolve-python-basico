from entities.product import Product

def create_product(products, name, price, quantity):
    """
    Cria um novo produto.
    Entrada: Lista de produtos, name, price, quantity.
    Saída: O novo Product.
    """
    product_id = str(len(products) + 1)
    new_prod = Product(product_id, name, price, quantity)
    products.append(new_prod)
    return new_prod

def read_products(products):
    """
    Retorna lista de produtos.
    Entrada: Lista de produtos.
    Saída: Lista de produtos.
    """
    return products

def update_product(products, product_id, new_name=None, new_price=None, new_quantity=None):
    """
    Atualiza um produto.
    Entrada: Lista de produtos, product_id, novos valores opcionais.
    Saída: True se atualizado, False se não encontrado.
    """
    for prod in products:
        if prod.id == product_id:
            if new_name:
                prod.name = new_name
            if new_price is not None:
                prod.price = new_price
            if new_quantity is not None:
                prod.quantity = new_quantity
            return True
    return False

def delete_product(products, product_id):
    """
    Deleta um produto.
    Entrada: Lista de produtos, product_id.
    Saída: True se deletado, False se não encontrado.
    """
    original_length = len(products)
    products[:] = [p for p in products if p.id != product_id]
    return len(products) < original_length

def search_product(products, query):
    """
    Busca produto por ID ou nome.
    Entrada: Lista de produtos, query.
    Saída: Lista de produtos encontrados.
    """
    return [p for p in products if p.id == query or query.lower() in p.name.lower()]

def get_products_sorted_by_name(products):
    """
    Retorna produtos ordenados por nome.
    Entrada: Lista de produtos.
    Saída: Lista ordenada.
    """
    return sorted(products, key=lambda p: p.name)

def get_products_sorted_by_price(products):
    """
    Retorna produtos ordenados por preço.
    Entrada: Lista de produtos.
    Saída: Lista ordenada.
    """
    return sorted(products, key=lambda p: p.price)
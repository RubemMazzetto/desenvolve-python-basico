product1_name = input("Digite o nome do produto 1: ")
product1_price = float(input("Digite o preço unitário do produto 1: "))
product1_quantity = int(input("Digite a quantidade do produto 1: "))

product2_name = input("Digite o nome do produto 2: ")
product2_price = float(input("Digite o preço unitário do produto 2: "))
product2_quantity = int(input("Digite a quantidade do produto 2: "))

product3_name = input("Digite o nome do produto 3: ")
product3_price = float(input("Digite o preço unitário do produto 3: "))
product3_quantity = int(input("Digite a quantidade do produto 3: "))

total1 = product1_price * product1_quantity
total2 = product2_price * product2_quantity
total3 = product3_price * product3_quantity

total_price = total1 + total2 + total3

print(f"Total: R${total_price:,.2f}")
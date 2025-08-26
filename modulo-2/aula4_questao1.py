length = int(input("Digite o comprimento do terreno (em metros): "))

width = int(input("Digite a largura do terreno (em metros): "))

price_per_square_meter = float(input("Digite o preço por metro quadrado (em R$): "))

area_m2 = length * width

total_price = price_per_square_meter * area_m2

print(f"O terreno possui {area_m2}m2 e custa R${total_price:.2f}")
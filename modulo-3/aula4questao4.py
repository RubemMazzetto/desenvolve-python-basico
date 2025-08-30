distance_km = float(input("Digite a distância da entrega (em km): "))

weight_kg = float(input("Digite o peso do pacote (em kg): "))

if distance_km <= 100:
    rate_per_kg = 1.0
elif distance_km <= 300:
    rate_per_kg = 1.5
else:
    rate_per_kg = 2.0

base_freight = rate_per_kg * weight_kg

total_freight = base_freight + (10 if weight_kg > 10 else 0)

print(f"Valor do frete: R${total_freight:.2f}")
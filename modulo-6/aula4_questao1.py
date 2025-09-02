even_numbers = [x for x in range(20, 51, 2)]  # Pares de 20 a 50
squares = [x ** 2 for x in range(1, 10)]  # Quadrados de 1 a 9
div_by_seven = [x for x in range(1, 101) if x % 7 == 0]  # Divisíveis por 7
parity = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]  # Paridade

print("Números pares entre 20 e 50:", even_numbers)
print("Quadrados de [1, 9]:", squares)
print("Números divisíveis por 7 entre 1 e 100:", div_by_seven)
print("Paridade de range(0, 30, 3):", parity)
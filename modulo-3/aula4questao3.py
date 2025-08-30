year = int(input("Digite um ano: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Bissexto" if is_leap else "Não Bissexto")
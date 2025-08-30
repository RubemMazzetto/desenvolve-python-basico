first_number = int(input("Digite o primeiro número: "))

second_number = int(input("Digite o segundo número: "))

sum_result = first_number + second_number

is_even = sum_result % 2 == 0

print(f"A soma {sum_result} é {'par' if is_even else 'ímpar'}")
def collect_numbers():
    numbers = []
    print("Digite números inteiros (mínimo 4, digite 0 para finalizar):")
    while True:
        num = int(input())
        if num == 0:
            if len(numbers) < 4:
                print("Erro: Insira pelo menos 4 números antes de finalizar.")
                continue
            break
        numbers.append(num)
    return numbers

def print_list_analysis(numbers):
    print("Lista original:", numbers)
    print("3 primeiros elementos:", numbers[:3])
    print("2 últimos elementos:", numbers[-2:])
    print("Lista invertida:", numbers[::-1])
    print("Elementos de índices pares:", numbers[::2])
    print("Elementos de índices ímpares:", numbers[1::2])

number_list = collect_numbers()
print_list_analysis(number_list)
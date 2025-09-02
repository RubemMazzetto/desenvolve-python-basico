def print_name_staircase(name):
    for i in range(1, len(name) + 1):
        print(name[:i])

user_name = input("Digite seu nome: ")
print_name_staircase(user_name)
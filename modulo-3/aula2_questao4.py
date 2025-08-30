character_class = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()

strength = int(input("Digite os pontos de força (de 1 a 20): "))
magic = int(input("Digite os pontos de magia (de 1 a 20): "))

if character_class == "guerreiro":
    is_valid = strength >= 15 and magic <= 10
elif character_class == "mago":
    is_valid = strength <= 10 and magic >= 15
elif character_class == "arqueiro":
    is_valid = 5 < strength <= 15 and 5 < magic <= 15
else:
    is_valid = False

print("Pontos de atributo consistentes com a classe escolhida:", is_valid)
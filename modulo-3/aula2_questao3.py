age = int(input("Digite sua idade: "))

has_played_three_games = input("Já jogou pelo menos 3 jogos de tabuleiro? ").lower() == "true"

wins = int(input("Quantos jogos já venceu? "))

is_eligible = 16 <= age <= 18 and has_played_three_games and wins >= 1

print("Apto para ingressar no clube de jogos de tabuleiro:", is_eligible)
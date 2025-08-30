gender = input("Digite seu gênero (M ou F): ").upper()

age = int(input("Digite sua idade: "))

service_years = int(input("Digite seu tempo de serviço (em anos): "))

can_retire = (
    (gender == "F" and age > 60) or
    (gender == "M" and age > 65) or
    (service_years >= 30) or
    (age >= 60 and service_years >= 25)
)

print(can_retire)
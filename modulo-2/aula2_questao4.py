balance = 500.0
interest_rate = 1.01

for _ in range(3):
    balance *= interest_rate

print("Após 3 meses meu novo saldo é")
print(balance)
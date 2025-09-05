import csv
import os
from entities.user import User

USERS_FILE = 'users.csv'

class UserRepository:
    def load_users(self):
        """
        Carrega os usuários do arquivo CSV para uma lista de User.
        Saída: Lista de User.
        """
        users = []
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    users.append(User(row['username'], row['password'], row['role']))
        return users

    def save_users(self, users):
        """
        Salva a lista de User no arquivo CSV.
        Entrada: Lista de User.
        """
        with open(USERS_FILE, mode='w', newline='') as file:
            fieldnames = ['username', 'password', 'role']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow({'username': user.username, 'password': user.password, 'role': user.role})
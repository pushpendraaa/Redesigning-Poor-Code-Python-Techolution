import json
from user import User

class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filename, 'r') as f:
                users_data = json.load(f)
                return [User(**user) for user in users_data]
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.filename, 'w') as f:
            json.dump([user.__dict__ for user in self.users], f)

    def add_user(self,name,user_id):
        if any(user.user_id == user_id for user in self.users):
            return "User with this ID already exists."
        new_user = User(name, user_id)
        self.users.append(new_user)
        self.save_users()
        return "User added successfully."

    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_users()
                return "User removed successfully."
        return "User not found."

    def list_users(self):
        return "\n".join(str(user) for user in self.users if user)

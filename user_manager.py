import json
from user import User 

class UserManager:
    def __init__(self, filename='users.json'):
        """
        Constructor method to initialize a UserManager object.
        Args:
            filename (str): The name of the JSON file to load/save user data.
        """
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        """
        Load users data from a JSON file.
        Returns:
            list: A list of User objects loaded from the JSON file.
        """
        try:
            with open(self.filename, 'r') as f:
                users_data = json.load(f)
                return [User(**user) for user in users_data]
        except FileNotFoundError:
            return []

    def save_users(self):
        # Save users data to a JSON file.
        with open(self.filename, 'w') as f:
            json.dump([user.__dict__ for user in self.users], f)

    def add_user(self, name, user_id):
        """
        Add a new user to the collection.
        Args:
            name (str): The name of the user.
            user_id (str or int): The ID of the user.
        Returns:
            str: A message indicating the success or failure of the operation.
        """
        if any(user.user_id == user_id for user in self.users):
            return "User with this ID already exists."
        new_user = User(name, user_id)
        self.users.append(new_user)
        self.save_users()
        return "User added successfully."

    def remove_user(self, user_id):
        """
        Remove a user from the collection by user ID.
        Args:
            user_id (str or int): The ID of the user to remove.
        Returns:
            str: A message indicating the success or failure of the operation.
        """
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_users()
                return "User removed successfully."
        return "User not found."

    def list_users(self):
        """
        Generate a string containing details of all users in the collection.
        Returns:
            str: A formatted string containing details of all users.
        """
        return "\n".join(str(user) for user in self.users if user)

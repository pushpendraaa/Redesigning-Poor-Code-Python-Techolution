class User:
    def __init__(self, name, user_id):
        """
        Constructor method to initialize a User object.
        Args:
            name (str): The name of the user.
            user_id (str or int): The unique identifier of the user.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """
        String representation of the User object.
        Returns:
            str: A string representation of the user in the format "User: , ID: ".
        """
        return f"User: {self.name}, ID: {self.user_id}"

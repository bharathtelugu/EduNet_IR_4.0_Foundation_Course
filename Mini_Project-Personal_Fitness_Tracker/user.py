# Create a class to manage user accounts.
class User:
    def __init__(self, name):
        self.name = name
        self.workouts = []

    def __str__(self):
        return f"User: {self.name}"

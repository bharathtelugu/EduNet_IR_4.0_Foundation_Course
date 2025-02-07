# Functions to save and load user data.
import json
from user import User
from workout import Workout

def save_user_data(user, filename="user_data.json"):
    with open(filename, "w") as file:
        data = {
            "name": user.name,
            "workouts": [workout.__dict__ for workout in user.workouts]
        }
        json.dump(data, file)

def load_user_data(filename="user_data.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            user = User(data["name"])
            user.workouts = [Workout(**workout) for workout in data["workouts"]]
            return user
    except FileNotFoundError:
        return None

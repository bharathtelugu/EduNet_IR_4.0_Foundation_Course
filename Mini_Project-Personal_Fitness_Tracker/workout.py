# Define the Workout class and functions to add and view workouts.
class Workout:
    def __init__(self, date, workout_type, duration, calories_burned):
        self.date = date
        self.workout_type = workout_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date} - {self.workout_type}: {self.duration} mins, {self.calories_burned} cal"

# Generate daily workout reports.
def generate_daily_report(user):
    report = {}
    for workout in user.workouts:
        if workout.date not in report:
            report[workout.date] = {"duration": 0, "calories_burned": 0}
        report[workout.date]["duration"] += workout.duration
        report[workout.date]["calories_burned"] += workout.calories_burned

    return report

def display_report(report):
    for date, data in report.items():
        print(f"Date: {date}")
        print(f"  Total Duration: {data['duration']} mins")
        print(f"  Total Calories Burned: {data['calories_burned']} cal")

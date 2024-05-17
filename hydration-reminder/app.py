import time
from plyer import notification

def remind_to_drink_water(interval_minutes):
    while True:
        notification.notify(
            title="Hydration Reminder",
            message="It's time to drink water!",
            timeout=10
        )
        time.sleep(interval_minutes * 60)  # Send reminder after interval_minutes

def calculate_water_per_hour(water_goal):
    total_hours = 24
    water_per_hour = water_goal / total_hours
    return water_per_hour

def analyze_water_goal(water_goal):
    if water_goal < 2500:
        print("Your daily water intake goal is less than the recommended 2.5 liters. Remember to stay hydrated!")
    elif water_goal == 2500:
        print("Your daily water intake goal is equal to the recommended 2.5 liters. Keep it up!")
    else:
        print("Your daily water intake goal is greater than the recommended 2.5 liters. That's great!") 

def main():
    print("Welcome to Hydration Reminder!")
    print("--------------------------------")

    while True:
        try:
            water_goal = int(input("Enter your daily water intake goal (in ml): "))
            if water_goal <= 0:
                raise ValueError("Water goal must be a positive integer.")
            break 
        except ValueError as ve:
            print(f"Error: {ve}")

    while True:
        try:
            reminder_interval = int(input("Enter reminder interval (in minutes): "))
            if reminder_interval <= 0:
                raise ValueError("Reminder interval must be a positive integer.")
            break 
        except ValueError as ve:
            print(f"Error: {ve}")

    print("--------------------------------")

    water_per_hour = calculate_water_per_hour(water_goal)
    print(f"To meet your daily water intake goal of {water_goal} ml:")
    print(f"You should aim to drink approximately {water_per_hour:.2f} ml of water per hour.")
    print("--------------------------------")

    analyze_water_goal(water_goal)

    print("--------------------------------")

    print("Hydration reminders will be sent throughout the day.")
    remind_to_drink_water(reminder_interval)

if __name__ == "__main__":
    main()

import time
from plyer import notification

def remind_to_drink_water(interval_minutes):
    """
    Sends a notification to remind the user to drink water at specified intervals.
    
    Parameters:
    interval_minutes (int): The interval in minutes at which reminders should be sent.
    """
    while True:
        # Send a notification reminding the user to drink water
        notification.notify(
            title="Hydration Reminder",
            message="It's time to drink water!",
            timeout=10  # Notification stays on screen for 10 seconds
        )
        # Wait for the specified interval before sending the next reminder
        time.sleep(interval_minutes * 60)

def calculate_water_per_hour(water_goal):
    """
    Calculates the amount of water to drink per hour to meet the daily goal.
    
    Parameters:
    water_goal (int): The daily water intake goal in milliliters.
    
    Returns:
    float: The amount of water to drink per hour.
    """
    total_hours = 24  # Number of hours in a day
    water_per_hour = water_goal / total_hours  # Divide the daily goal by the total hours
    return water_per_hour

def analyze_water_goal(water_goal):
    """
    Analyzes the user's water intake goal and provides feedback.
    
    Parameters:
    water_goal (int): The daily water intake goal in milliliters.
    """
    if water_goal < 2500:
        print("Your daily water intake goal is less than the recommended 2.5 liters. Remember to stay hydrated!")
    elif water_goal == 2500:
        print("Your daily water intake goal is equal to the recommended 2.5 liters. Keep it up!")
    else:
        print("Your daily water intake goal is greater than the recommended 2.5 liters. That's great!") 

def main():
    """
    Main function to run the hydration reminder program. Prompts the user for input and sets up reminders.
    """
    print("Welcome to Hydration Reminder!")
    print("--------------------------------")

    # Prompt user for their daily water intake goal
    while True:
        try:
            water_goal = int(input("Enter your daily water intake goal (in ml): "))
            if water_goal <= 0:
                raise ValueError("Water goal must be a positive integer.")
            break  # Exit loop if input is valid
        except ValueError as ve:
            print(f"Error: {ve}")

    # Prompt user for the reminder interval in minutes
    while True:
        try:
            reminder_interval = int(input("Enter reminder interval (in minutes): "))
            if reminder_interval <= 0:
                raise ValueError("Reminder interval must be a positive integer.")
            break  # Exit loop if input is valid
        except ValueError as ve:
            print(f"Error: {ve}")

    print("--------------------------------")

    # Calculate and display the amount of water to drink per hour
    water_per_hour = calculate_water_per_hour(water_goal)
    print(f"To meet your daily water intake goal of {water_goal} ml:")
    print(f"You should aim to drink approximately {water_per_hour:.2f} ml of water per hour.")
    print("--------------------------------")

    # Analyze the user's water goal and provide feedback
    analyze_water_goal(water_goal)
    print("--------------------------------")

    print("Hydration reminders will be sent throughout the day.")
    
    # Start sending hydration reminders at the specified interval
    remind_to_drink_water(reminder_interval)

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly

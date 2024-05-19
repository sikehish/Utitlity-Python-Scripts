import time
from datetime import datetime
from plyer import notification

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

def input_task():
    """
    Prompt the user to input task description and task time.
    
    Returns:
    tuple: A tuple containing task description and task time.
    """
    task_desc = input("Enter the task description: ")
    task_time = input("Enter the task time (HH:MM, 24-hour format): ")
    return task_desc, task_time

def validate_time(task_time):
    """
    Validate the format of the input task time and convert it to a datetime object.
    
    Parameters:
    task_time (str): The input task time in HH:MM format.
    
    Returns:
    datetime: The validated datetime object representing the task time, or None if format is invalid.
    """
    try:
        # Parse the input task time into a datetime object
        task_datetime = datetime.strptime(task_time, "%H:%M")
        
        # Extract current date and time
        now = datetime.now()
        
        # Replace year, month, and day of task_datetime with current values
        task_datetime = task_datetime.replace(year=now.year, month=now.month, day=now.day)
        
        # If task time has already passed today, schedule it for the next day
        if task_datetime < now:
            task_datetime = task_datetime.replace(day=now.day + 1)
        
        return task_datetime
    except ValueError:
        return None

def set_timer(task_desc, task_datetime):
    """
    Set a timer to send a notification for the specified task at the given time.
    
    Parameters:
    task_desc (str): The description of the task.
    task_datetime (datetime): The datetime object representing the task time.
    """
    # Calculate time difference between current time and task time
    now = datetime.now()
    time_diff = (task_datetime - now).total_seconds()
    
    # Print scheduled task details and time until notification
    print(f"Task '{task_desc}' scheduled at {task_datetime}. Notification will be sent in {time_diff} seconds.")
    
    # Wait until it's time to send the notification
    time.sleep(time_diff)
    
    # Send notification for the task
    send_notification(task_desc)

def send_notification(task_desc):
    """
    Send a notification to remind the user about the task.
    
    Parameters:
    task_desc (str): The description of the task.
    """
    # Initialize pygame mixer for sound
    pygame.mixer.init()

    notification.notify(
        title="Task Reminder",
        message=f"Time to: {task_desc}",
        timeout=10  # Notification stays on screen for 10 seconds
    )

    # Play the sound notification
    pygame.mixer.music.load("reminder_finish_task.mp3")  # Replace "reminder_finish_task.mp3" with your sound file
    # # OR
    # pygame.mixer.music.load("reminder_sound.mp3")

    pygame.mixer.music.play()

    time.sleep(10)
        

def main():
    """
    Main function to input task details, validate time, and set timer for task notification.
    """
    # Prompt user to input task details
    task_desc, task_time = input_task()
    
    # Validate the input task time
    task_datetime = validate_time(task_time)
    
    # Keep prompting until valid time format is entered
    while task_datetime is None:
        print("Invalid time format. Please enter time in HH:MM format.")
        task_time = input("Enter the task time (HH:MM, 24-hour format): ")
        task_datetime = validate_time(task_time)
    
    # Set timer for the task notification
    set_timer(task_desc, task_datetime)

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly

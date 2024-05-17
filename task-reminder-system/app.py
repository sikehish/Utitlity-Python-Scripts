import time
from datetime import datetime
from plyer import notification

def input_task():
    task_desc = input("Enter the task description: ")
    task_time = input("Enter the task time (HH:MM, 24-hour format): ")
    return task_desc, task_time

def validate_time(task_time):
    try:
        task_datetime = datetime.strptime(task_time, "%H:%M")
        # ALWAYS REMEMBER: The resulting task_datetime object contains the date as January 1, 1900, so we need to replace the year month and day witht he current year month and day
        print(task_datetime)
        now = datetime.now()
        task_datetime = task_datetime.replace(year=now.year, month=now.month, day=now.day)
        print(task_datetime, now)
        if task_datetime < now:
            task_datetime = task_datetime.replace(day=now.day + 1)
        return task_datetime
    except ValueError:
        return None

def set_timer(task_desc, task_datetime):
    now = datetime.now()
    time_diff = (task_datetime - now).total_seconds()
    print(f"Task '{task_desc}' scheduled at {task_datetime}. Notification will be sent in {time_diff} seconds.")
    time.sleep(time_diff)
    send_notification(task_desc)

def send_notification(task_desc):
    notification.notify(
        title="Task Reminder",
        message=f"Time to: {task_desc}",
        timeout=10
    )

def main():
    task_desc, task_time = input_task()
    task_datetime = validate_time(task_time)
    while task_datetime is None:
        print("Invalid time format. Please enter time in HH:MM format.")
        task_time = input("Enter the task time (HH:MM, 24-hour format): ")
        task_datetime = validate_time(task_time)
    set_timer(task_desc, task_datetime)

if __name__ == "__main__":
    main()

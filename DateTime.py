from datetime import datetime


def TimeDateCur():

    now = datetime.now()  # Get the current date and time
    current_time = now.strftime('%Y-%m-%d %H:%M:%S') # Format the date and time 34-hrt fmt

    return current_time  # Example output: '2024-09-26 02:15:30 PM'

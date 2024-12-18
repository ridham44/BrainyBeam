#Write a function which will return the all the Tuesday and Friday dates by taking month as a input.
#Ridham Patel
#15/12/2024

import calendar
from datetime import datetime

def get_tuesdays_and_fridays(year, month):
    try:
        first_day, num_days = calendar.monthrange(year, month)
        dates = []

        for day in range(1, num_days + 1):
            weekday = calendar.weekday(year, month, day)

            if weekday in (1, 4):
                # Add the date YYYY-MM-DD format
                dates.append(datetime(year, month, day).strftime("%Y-%m-%d"))
                
        return dates

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    result = get_tuesdays_and_fridays(year, month)
    print("Tuesdays and Fridays:")
    
    for date in result:
        print(date)

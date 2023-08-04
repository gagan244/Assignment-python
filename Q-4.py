import calendar
from datetime import datetime

def season_and_leap_year():
    # Take the year, month and day from user
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))

    # Determine the season
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    date = datetime(year, month, day)
    season = seasons[(date.month%12 + 3)//3 - 1]
    print(f"The season on {year}-{month}-{day} is {season}.")

    # Check if year is a leap year
    if calendar.isleap(year):
        print(f"{year} is a leap year. It has 366 days.")
    else:
        print(f"{year} is not a leap year.")
        next_year = year
        while not calendar.isleap(next_year):
            next_year += 1
        print(f"The next leap year is {next_year}.")

season_and_leap_year()

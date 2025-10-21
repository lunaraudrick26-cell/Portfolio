# Exercise 5: Days of the Month - 30 Marks
# Program to tell users how many days are in a specific month

# Dictionary mapping month numbers to days
days_in_month = {
    1: 31,   # January
    2: 28,   # February (non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Get month number from user
month = int(input("Enter the month number (1-12): "))

# Check if input is valid
if month in days_in_month:
    # Advanced Requirement: Check for leap year if February
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            print(f"February has 29 days in a leap year.")
        else:
            print(f"February has {days_in_month[month]} days.")
    else:
        print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")